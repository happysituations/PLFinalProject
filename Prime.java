import java.util.*;

public class Prime
{
    public static void main (String[] args)
    {
        int i =0;
        int num =0;

        ArrayList<List<Object>> primes = new ArrayList<List<Object>>();

        for (i = 1; i <= 100; i++)
        {
            int counter=0;
            for(num =i; num>=1; num--)
            {
                if(i%num==0)
                {
                    counter = counter + 1;
                }
            }
            if (counter ==2)
            {
                primes = primes.append(i);
            }
        }
        System.out.println("Prime numbers from 1 to 100 are :");
        System.out.println(primes);
    }
    public static int a() { return primes; }
}
