public class Write (

  public static void main(String[] args) throws Exception {
    file f = new file("fileDirectory.xls");
    WritableWorkbook myexcel = Workbook.createWorkbook (f);
    WritableSheet mysheet = myexel.createSheet("mySheet",0);
    Label 1 = new Label(0, 0, "data 1");
    mysheet.addCell(1);
    myexel.write();
    myexel.close();
   
   }
   
   //https://www.youtube.com/watch?v=OHodZArY9ns
   
   
   
 