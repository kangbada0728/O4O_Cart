package doo;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import javax.imageio.ImageIO;
import com.google.zxing.BinaryBitmap;
import com.google.zxing.ChecksumException;
import com.google.zxing.EncodeHintType;
import com.google.zxing.FormatException;
import com.google.zxing.NotFoundException;
import com.google.zxing.Result;
import com.google.zxing.WriterException;
import com.google.zxing.client.j2se.BufferedImageLuminanceSource;
import com.google.zxing.common.HybridBinarizer;
import com.google.zxing.multi.qrcode.QRCodeMultiReader;
import com.google.zxing.qrcode.decoder.ErrorCorrectionLevel;

public class QRCode {
	
	private static QRCode QR;
	public static QRCode getInstance() {
		if (QR == null) {
			QR = new QRCode();
		}
		return QR;
	}
	
	static Result[] qrCodeResult;
	private static ArrayList<Integer> x_location = new ArrayList<>();
	private static ArrayList<Integer> y_location = new ArrayList<>();

	public void setLocation(int x, int y) {
		QRCode.x_location.add(x);
		QRCode.y_location.add(y);
	}

	public static void main(String[] args)
			throws WriterException, IOException, NotFoundException, ChecksumException, FormatException {

		// String charset = "UTF-8"; // or "ISO-8859-1"
		

		// readmQRCode("C:\\Users\\HG\\origin.png", charset, hintMap);
		if (args.length == 1) {
			System.out.print(args[0].charAt(0)+",");
			String path = System.getProperty("user.dir") + "\\image\\" + args[0];
			//readmQRCode(path);
			for (int qr = 0; qr < qrCodeResult.length; qr++) {
				System.out.print(qrCodeResult[qr].getText()+",");
				System.out.print(QRCode.getInstance().x_location.get(qr)+",");
				System.out.println(QRCode.getInstance().y_location.get(qr)+",");
			}

		} else {
			System.out.println("usage : java -jar finder.jar imagename.jpg");

			String a = "1asapple";
			System.out.println(a.charAt(0)+",");
			String path = "C:\\Users\\HG\\origin.png";
			readmQRCode(path);
			for (int qr = 0; qr < qrCodeResult.length; qr++) {
				System.out.print(qrCodeResult[qr].getText()+",");
				System.out.print(QRCode.getInstance().x_location.get(qr)+",");
				System.out.println(QRCode.getInstance().y_location.get(qr)+",");
			}
			//cart ID, X,Y
		}

	}

	public static void readmQRCode(String path)
			throws FileNotFoundException, IOException, NotFoundException, ChecksumException, FormatException {
		Map hintMap = new HashMap();
		
		hintMap.put(EncodeHintType.ERROR_CORRECTION, ErrorCorrectionLevel.L);
		
		BinaryBitmap binaryBitmap = new BinaryBitmap(
				new HybridBinarizer(new BufferedImageLuminanceSource(ImageIO.read(new FileInputStream(path)))));
		
		qrCodeResult = new QRCodeMultiReader().decodeMultiple(binaryBitmap, hintMap);
	}


}
