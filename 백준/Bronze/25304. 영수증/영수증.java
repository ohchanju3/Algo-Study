import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int x = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        

        int sum = 0;
        
        for (int i=0; i<n; i++){
            String str = br.readLine();
            StringTokenizer st = new StringTokenizer(str, " ");
        
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            sum += (a*b);
            }
        if (sum==x){
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
        
    }
}