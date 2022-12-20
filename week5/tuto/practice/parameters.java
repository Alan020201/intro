class parameters{
 public void display1(){
 System.out.println("Method without parameter");
}
public void display2(int a){
    System.out.println("method with a single parameter:"+a);
}
public static void main(String[]args){
Main obj = new Main();
obj.display1();
obj.display2(26);    
}
}