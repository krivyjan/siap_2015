import org.bouncycastle.tsp.TimeStampResponse;
import org.bouncycastle.util.encoders.Base64;

public class TimeStampFactory {

    public static void main(String[] args) throws Exception {
        String data = args[0];
        TimeStampResponse response = new TimeStampResponse(Base64.decode(data));
        String encResponse = new String(Base64.encode(response.getTimeStampToken().getEncoded()));

        System.out.println(encResponse);

        return;
    }
}