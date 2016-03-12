import java.io.*;
import jxl.Workbook;
import jxl.write.WritableCell;
import jxl.write.WritableSheet;
import jxl.write.WritableWorkbook;
import java.awt.Label;

public class NoteReader {

	public static void main(String[] args)  {
		int count=0;
		  try{
			  FileInputStream fstream = new FileInputStream("output.txt");
			  DataInputStream in = new DataInputStream(fstream);
			  BufferedReader br = new BufferedReader(new InputStreamReader(in));
			  String strLine;
			  //Reads the note line
			  while ((strLine = br.readLine()) != null)   {
				  count++;//counts each line, this will represent as the col
				  String[] info = strLine.split(",");//split the values
				  String note = info[0];//First value is the note
	              String length = info[1];//second value is the length of note
	              
	              
	             //turn the notes into row value, so the matrix will know where to put the note in the row\
	              
	              //create matrix
	              String [ ] [ ] noteSheet = new String [ 8 ] [ count ] ; //create memory space for entire matrix              
	              
	              
	              
	              //print
	              System.out.println (strLine);
	              System.out.println ("amount of expected colums: "+ count);
	              System.out.println ("Notes: "+ note + " length: "+ length);
			  }
			  
			  in.close();
			    }catch (Exception e){//Catch exception if any
			  System.err.println("Error: " + e.getMessage());
			  }
		  }
	}
