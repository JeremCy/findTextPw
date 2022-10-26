import java.io.IOException;
import java.util.Scanner;

public class App {
   
    public static void main(String[] args) throws IOException{
        try (Scanner in = new Scanner(System.in)) {
            System.out.print("Entrez le path du fichier a scanner : ");
            String readfile = in.nextLine();
            System.out.print("Entrez le path du fichier result : ");
            String writefile = in.nextLine();
            System.out.print("Enter the regex you want to search (tap enter to stop adding regex):");
            String regex = in.nextLine();

            new Converter(readfile,writefile,regex);
        }
    }

}

	