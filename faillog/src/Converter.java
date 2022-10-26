import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Converter {
    // A method that takes in three parameters, readfile, writefile, and regex. It then creates a new file
// with the name of writefile and the extension of .csv. It then reads the readfile and writes the
// contents of the file to the new file.
    public  Converter(String readfile,String writefile,String regex) throws IOException{
        if (regex == ""){
            regex = "^[0-9]{6,7}";
        }   
        try (BufferedWriter out = new BufferedWriter(new FileWriter(writefile+".csv"))) {
            try (BufferedReader reader = new BufferedReader(new FileReader(readfile))) {
                String line = reader.readLine();
                Pattern p = Pattern.compile(regex);
                while(line != null){
                    Matcher m = p.matcher(line);
                    if (m.find()) {
                        //while(m.find()) {
                            //System.out.println(m.group());
                            //out.write(m.group());
                            //out.newLine();
                        //}
                        out.write(line);
                        out.newLine();
                    }
                    line = reader.readLine();        
                }
            }catch (IOException e) {
                e.printStackTrace();
            }          
        } catch (IOException e) {
            e.printStackTrace();
        }
    }      
}
