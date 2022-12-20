class lamp{
    boolean isOn;
    void turnOn(){
        isOn=true;
        System.out.println("Light on? " + isOn);
    }
    void turnoff(){
        isOn=false;
        System.out.println("Light on? "+ isOn);
    }
    }
    class Main{
        public static void main (String[] args){
            lamp led = new lamp();
            lamp halogen = new lamp();
            led.turnOn();
            halogen.turnoff();

        }

        public Object display1() {
            return null;
        }

        public void display2(int i) {
        }
    }