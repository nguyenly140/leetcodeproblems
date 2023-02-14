import java.lang.Math;

public class fibo {
  public static int fib(int n) {
    double sqrt5 = Math.sqrt(5);
    return (int)((Math.pow(1 + sqrt5, n) - Math.pow(1 - sqrt5, n)) / (double)(Math.pow(2, n) * sqrt5));
  }

  public static void main(String[] args) {
    System.out.println("F(0) = " + fib(0) + "\nF(1) = " + fib(1) + "\nF(2) = " + fib(2) + "\nF(3) = " + fib(3) + "\nF(4) = " + fib(4));
  }
}
