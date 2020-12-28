
/* Modelo de Código para Controle de Carro c/ Arduino */
 
// Definir os pinos de utilização do Driver L298.
int f1 = 5; //forward of the right motor
int f1Value = 0; //value for the power of f1
int b1 = 6; //backward of the right motor
int b1Value = 0; //value for the power of b1
int f2 = 9; //forward of the left motor
int f2Value = 0; //value for the power of f2
int b2 = 10; //backward of the left motor
int b2Value = 0; //value for the power of b2

// Variáveis Úteis
int state_temp;
int vSpeed = 200;   // Define velocidade padrão 0 - 255.
int maxSpeed = 255; // Velocidade máxima
char state;
 
void setup() {
  // Inicializar as portas como entrada e saída.
  pinMode(f1, OUTPUT);
  pinMode(f2, OUTPUT);
  pinMode(b1, OUTPUT);
  pinMode(b2, OUTPUT);

  // Inicializar a comunicação serial.
  Serial.begin(9600);
  
}
 
void loop() {
 
  // Salva os valores da variável 'state'
  if (Serial.available() > 0) {
    state_temp = Serial.read();
    state = state_temp;
  }
  
  // this assures us that we won't have forward and backward
  // signals being sent at the same time (and makes our code cleaner)
  if(f1Value != 0){
    b1Value == 0;
    analogWrite(b1, b1Value);
  }

  else if(b1Value != 0){
    f1Value == 0;
    analogWrite(f1, f1Value);
  }

  if(f2Value != 0){
    b2Value == 0;
    analogWrite(b2, b2Value);
  }

  else if(b2Value != 0){
    f2Value == 0;
    analogWrite(f2, f2Value);
  }


  // Se o estado recebido for igual a '8', o carro se movimenta para frente.
  if (state == '8') {
    Serial.println("Comando para Frente");
    // Comandos de Motores
    f1Value = maxSpeed;
    f2Value = maxSpeed;
    analogWrite(f1, f1Value);
    analogWrite(f2, f2Value);

  }
    // Se o estado recebido for igual a '7', o carro se movimenta para Frente Esquerda.
    else if (state == '7') {  
      Serial.println("Comando para Frente-Esquerda");
      // Comandos de Motores
      f1Value = maxSpeed;
      f2Value = vSpeed;
      analogWrite(f1, f1Value);
      analogWrite(f2, f2Value);
      
  }
    // Se o estado recebido for igual a '9', o carro se movimenta para Frente Direita.
    else if (state == '9') {   
    Serial.println("Comando para Frente-Direita");
      // Comandos de Motores
      f1Value = vSpeed;
      f2Value = maxSpeed;
      analogWrite(f1, f1Value);
      analogWrite(f2, f2Value);
  }
  // Se o estado recebido for igual a '2', o carro se movimenta para trás.
  else if (state == '2') { 
    Serial.println("Comando para Trás");
      // Comandos de Motores
      b1Value = maxSpeed;
      b2Value = maxSpeed;
      analogWrite(b1, b1Value);
      analogWrite(b2, b2Value);

  }
   // Se o estado recebido for igual a '1', o carro se movimenta para Trás Esquerda.
   else if (state == '1') {  
    Serial.println("Comando para Trás-Esquerda");
      // Comandos de Motores
      b1Value = maxSpeed;
      b2Value = vSpeed;
      analogWrite(b1, b1Value);
      analogWrite(b2, b2Value);
  }
  // Se o estado recebido for igual a '3', o carro se movimenta para Trás Direita.
  else if (state == '3') {  
    Serial.println("Comando para Trás-Direita");
      // Comandos de Motores
      b1Value = vSpeed;
      b2Value = maxSpeed;
      analogWrite(b1, b1Value);
      analogWrite(b2, b2Value);
  }
  // Se o estado recebido for igual a '4', o carro se movimenta para esquerda.
  else if (state == '4') {   
    Serial.print("Comando para Esquerda");
      // Comandos de Motores
      f1Value = maxSpeed;
      b2Value = maxSpeed;
      analogWrite(f1, f1Value);
      analogWrite(b2, b2Value);
  }
  // Se o estado recebido for igual a '6', o carro se movimenta para direita.
  else if (state == '6') {   
    Serial.println("Comando para Direita");
      // Comandos de Motores
      f2Value = maxSpeed;
      b1Value = maxSpeed;
      analogWrite(f2, f2Value);
      analogWrite(b1, b1Value);
  }
  // Se o estado recebido for igual a '5', o carro permanece parado.
  else if (state == '5') {   
    Serial.print("Comando para Parar");
      f1Value = 0;
      f2Value = 0;
      b1Value = 0;
      b2Value = 0;
      analogWrite(f1, f1Value);
      analogWrite(f2, f2Value);
      analogWrite(b1, b1Value);
      analogWrite(b2, b2Value);
  }
}
