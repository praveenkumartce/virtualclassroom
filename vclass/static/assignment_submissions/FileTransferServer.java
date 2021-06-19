import java.io.*;
import java.net.*;

public class FileTransferServer { 
    
    public static void main(String[] args) throws Exception {
        ServerSocket ssock = new ServerSocket(400);
        Socket socket = ssock.accept();
        System.out.println("Connection established with client");
        InetAddress IA = InetAddress.getByName("localhost"); 
        
        File file = new File("C:/Users/prave/Documents/18C072 Netwok Lab Terminal/source.txt");
        FileInputStream fis = new FileInputStream(file);
        BufferedInputStream bis = new BufferedInputStream(fis); 
          
        //Get socket's output stream
        OutputStream os = socket.getOutputStream();
                
        //Read File Contents into contents array 
        byte[] contents;
        long fileLength = file.length(); 
        long current = 0;
         
        long start = System.nanoTime();
        while(current!=fileLength){ 
            int size = 10000;
            if(fileLength - current >= size)
                current += size;    
            else{ 
                size = (int)(fileLength - current); 
                current = fileLength;
            } 
            contents = new byte[size]; 
            bis.read(contents, 0, size); 
            os.write(contents);
            System.out.print("Sending file ... "+(current*100)/fileLength+"% complete!\n");
        }   
        
        os.flush(); 
        //File transfer done. Close the socket connection!
        socket.close();
        ssock.close();
        System.out.println("Source File sent successfully!");
    }
}