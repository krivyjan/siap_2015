import org.bouncycastle.tsp.TimeStampResponse;
import org.bouncycastle.util.encoders.Base64;

public class TimeStampFactory {

    public static String getTimeStamp(byte[] data) throws Exception {
        TimeStampResponse response = new TimeStampResponse(Base64.decode(data));
        String encResponse = new String(Base64.encode(response.getTimeStampToken().getEncoded()));

        return encResponse;
    }
}