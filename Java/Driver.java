import java.util.Scanner;

public class Driver {
	static void ReverseDigits(int n) {
		String s = Integer.toString(n);

		for(int i = s.length()-1; i >= 0; i--) {
			System.out.print(s.charAt(i));
		}
	}

	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);

		scan.close();
	}

}
