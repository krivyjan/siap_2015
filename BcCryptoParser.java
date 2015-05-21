import java.io.ByteArrayInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.cert.CRL;
import java.security.cert.Certificate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.Iterator;

import org.bouncycastle.tsp.TimeStampResponse;
import org.bouncycastle.util.encoders.Base64;
import org.bouncycastle.asn1.ASN1InputStream;
import org.bouncycastle.asn1.ASN1ObjectIdentifier;
import org.bouncycastle.asn1.ASN1Primitive;
import org.bouncycastle.asn1.ASN1Sequence;
import org.bouncycastle.asn1.DERBitString;
import org.bouncycastle.asn1.ocsp.Signature;
import org.bouncycastle.asn1.pkcs.CRLBag;
import org.bouncycastle.asn1.tsp.MessageImprint;
import org.bouncycastle.asn1.util.ASN1Dump;
import org.bouncycastle.asn1.x509.AlgorithmIdentifier;
import org.bouncycastle.cert.X509CertificateHolder;
import org.bouncycastle.cms.CMSException;
import org.bouncycastle.cms.CMSSignedData;
import org.bouncycastle.jcajce.provider.asymmetric.x509.CertificateFactory;
import org.bouncycastle.tsp.TSPException;
import org.bouncycastle.tsp.TimeStampRequest;
import org.bouncycastle.tsp.TimeStampRequestGenerator;
import org.bouncycastle.tsp.TimeStampResponse;
import org.bouncycastle.tsp.TimeStampResponseGenerator;
import org.bouncycastle.tsp.TimeStampToken;
import org.bouncycastle.tsp.TimeStampTokenInfo;
import org.bouncycastle.util.Store;
import org.bouncycastle.util.encoders.Base64;
import org.bouncycastle.asn1.x509.SubjectPublicKeyInfo;

public class BcCryptoParser {
	
	public static InputStream getCrlInputStream() throws IOException {
		InputStream input = null;
		FileOutputStream output = null;
		URL url = new URL("http://test.monex.sk/DTCCACrl/DTCCACrl.crl");
		try {
			URLConnection connection = url.openConnection();

			input = connection.getInputStream();
			output = new FileOutputStream("./CRL.crl");

			byte[] buffer = new byte[4096];
			int length;

			while ((length = input.read(buffer)) > 0) {
				output.write(buffer, 0, length);
			}
		} finally {
			input.close();
			output.close();
		}
		Path path = Paths.get("./CRL.crl");
		byte[] crlFile = Files.readAllBytes(path);
		
		return new ByteArrayInputStream(crlFile);
	}
	
	public static void printHelp(){
		System.out.println("Usage:");
		System.out.println("java -jar BcCryptoParser.jar <CONTROL> <param1> [param2]");
		System.out.println("CONTROL == 0:");
		System.out.println("             param1 = ds:X509Certificate");
		System.out.println("             RETURNS: Subject, SerialNumber, Issuer, PublicKey");
		System.out.println("CONTROL == 1:");
		System.out.println("             param1 = xades:EncapsulatedTimeStamp");
		System.out.println("             param2 = ds:SignatureValue");
		System.out.println("             RETURNS: true/false, [REASON]");
		System.out.println("CONTROL == 2:");
		System.out.println("             param1 = xades:EncapsulatedTimeStamp");
		System.out.println("             param2 = ds:X509Certificate");
		System.out.println("             RETURNS: true/false, [REASON]");
	}

    public static void main(String[] args) throws Exception, TSPException, CMSException {
		X509CertificateHolder certHolder = null;
		X509CertificateHolder signerCertificate = null;
		InputStream certificateStream = null;
		CertificateFactory certFactory = null;
		Certificate cert = null;
		CRL crl = null;
		TimeStampToken timestampToken = null;
		byte[] inputData = null;
		byte[] inputData2 = null;
		
		if(args.length == 0){
			printHelp();
			return;
		}
		try{
	    	switch(args[0]){
	    		// CORE VALIDATION
	    		case "0":
	    			byte[] signCertificate = Base64.decode(args[1]);
	    			certHolder = new X509CertificateHolder(signCertificate);
	    			
	    			System.out.println(certHolder.getSubject().toString());
	    			System.out.println(certHolder.getSerialNumber().toString());
	    			System.out.println(certHolder.getIssuer().toString());
	    			System.out.println(certHolder.getSubjectPublicKeyInfo().getPublicKeyData());
	    			
	    			break;
	    		// TIMESTAMP TIMESPAN VALIDATION
	    		case "1":
	    			// INITIALIZATION
	    			inputData = Base64.decode(args[1]); // TimeStampToken
	    			inputData2 = Base64.decode(args[2]); // SignatureValue
	    			timestampToken = new TimeStampToken(new CMSSignedData(inputData));
	    			
	    			// TIMESTAMP EXPIRATION CHECK
	    			@SuppressWarnings("unchecked")
					Store<X509CertificateHolder> tokenCertificates = timestampToken.getCertificates();
	    			ArrayList<X509CertificateHolder> certificates = new ArrayList<X509CertificateHolder>(tokenCertificates.getMatches(null));
	    			for(Iterator<X509CertificateHolder> i = certificates.iterator(); i.hasNext();) {
	    				certHolder = i.next();
	    				if (certHolder.getIssuer().toString().equals(timestampToken.getSID().getIssuer().toString()) &&
	    						certHolder.getSerialNumber().equals(timestampToken.getSID().getSerialNumber())
	    				) {
	    					signerCertificate = certHolder;
	    					break;
	    				}
	    			}
	    			byte[] certificate = signerCertificate.getEncoded();
	    			if (signerCertificate == null &&
	    				signerCertificate.getNotBefore().after(new Date()) ||
	    				signerCertificate.getNotAfter().before(new Date())
	    			) {
	    				System.out.println("false");
	    				System.out.println("Timestamp certificate is not yet valid or expired.");
	    				return;
	    			}
	
	    			// MESSAGE IMPRINT EQUALITY TEST
	    			TimeStampTokenInfo tokenInfo = timestampToken.getTimeStampInfo();
	                String algorithm = null;
	                switch (tokenInfo.getMessageImprintAlgOID().toString()) {
	                    case "2.16.840.1.101.3.4.2.4":
	                        algorithm = "SHA-224";
	                    break;
	                    case "2.16.840.1.101.3.4.2.1":
	                        algorithm = "SHA-256";
	                    break;
	                    case "2.16.840.1.101.3.4.2.2":
	                        algorithm = "SHA-384";
	                    break;
	                    case "2.16.840.1.101.3.4.2.3":
	                        algorithm = "SHA-512";
	                    break;
	                    default:
	        				System.out.println("false");
	                        System.out.println("Unsupported TimeStamp Token hash algorithm.");
	                        return;
	                }
	    			MessageDigest digest = MessageDigest.getInstance(algorithm);
	                digest.update(inputData2);
	                if(!Arrays.equals(digest.digest(), tokenInfo.getMessageImprintDigest())){
	                	System.out.println("false");
	                    System.out.println("Message imprint not equal to SignatureValue.");
	    				return;
	                }
	    			
	    			// CRL REVOCATION TEST
	    			certificateStream = new ByteArrayInputStream(certificate);
	    			certFactory = new CertificateFactory();
	    			crl = certFactory.engineGenerateCRL(getCrlInputStream());
	    			cert = certFactory.engineGenerateCertificate(certificateStream);
	    			if (crl.isRevoked(cert)) {
	    				System.out.println("false");
	    				System.out.println("TimeStamp certificate is revoked.");
	    				return;
	    			}
	    			
	    			// TEST PASSED
					System.out.println("true");
					break;
				// SIGNER CERTIFICATE VALIDATION
	    		case "2":
	    			// INITIALIZATION
	    			inputData = Base64.decode(args[1]); // TimeStampToken
	    			inputData2 = Base64.decode(args[2]); // SignatureValue
	    			timestampToken = new TimeStampToken(new CMSSignedData(inputData));
					signerCertificate = new X509CertificateHolder(inputData2);
			
					// CERTIFICATE EXPIRATION CHECK
					if (signerCertificate.getNotBefore().after(timestampToken.getTimeStampInfo().getGenTime()) ||
						signerCertificate.getNotAfter().before(timestampToken.getTimeStampInfo().getGenTime())
					) {
						System.out.println("false");
	    				System.out.println("Signer certificate is not yet valid or expired.");
	    				return;
					}
					
					// CRL REVOCATION TEST				
					certFactory = new CertificateFactory();
					certificateStream = new ByteArrayInputStream(inputData);
					cert = certFactory.engineGenerateCertificate(certificateStream);
					crl = certFactory.engineGenerateCRL(getCrlInputStream());
					if (crl.isRevoked(cert)) {
						System.out.println("false");
	    				System.out.println("Signer certificate is revoked.");
	    				return;
					}
	    			
	    			// TEST PASSED
					System.out.println("true");
	    		break;
	    	}
		} catch(Exception e){
			System.out.println("false");
			System.out.println(e.getMessage());
		}
    }
}