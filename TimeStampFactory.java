import org.bouncycastle.*;
import org.bouncycastle.asn1.tsp.TimeStampResp;
import org.bouncycastle.tsp.TimeStampRequest;
import org.bouncycastle.tsp.TimeStampResponse;
import org.bouncycastle.util.encoders.Base64;

public class TimeStampFactory {

    public static byte[] getTimeStamp(String strUrl,byte[] data,boolean calculateDigest,String digestAlgorithm) throws Exception {
      TimeStampResponse response = getTimeStampResponse(strUrl,data,calculateDigest,digestAlgorithm);
      PKIFailureInfo failure = response.getFailInfo();
      int value = (failure == null) ? 0 : failure.intValue();
      if (value != 0) {
        throw new Exception("Invalid TSA '" + strUrl + "' response, code "+ value);
      }
      TimeStampToken tsToken = response.getTimeStampToken();
      if (tsToken == null) {
        throw new Exception("Failed to return time stamp token");
      }
      byte[] encoded = tsToken.getEncoded();

      return encoded;
    }
}