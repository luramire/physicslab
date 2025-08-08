/*Sistema de Adquisición de datos para el Laboratorios Integrado de Fisica de la Universidad de Antioquia).
Está diseñado para el sistema basado en ChipKitUNO32 diseñado en I+D.

Implementa un juego de comandos que pueden ser enviados manualmente desde una consola serial ó desde la aplicación PHYSICSLAB
desarrollada para este sistema.
Tiempo muerto por envío serial: 0,07ms por caracter enviado (Usando baudrate=115200).
Programado por: Luis Felipe Ramirez Garcia, Instituto de Fisica, Universidad de Antioquia.
Revisado: 2025

VERSION PARA TARJETAS COLOR ROJO (Sensor de temperatura MAX6675)
*/

#define led1 34
#define led2 33
#define led3 32
#define led4 31

//PINES DEL SPI
#define MISOS 12
#define SCKS 13  
#define CSS 44

#define foto 7
#define foto2 8

int numero_funcion;

void setup(){
 pinMode(led1, OUTPUT);
 pinMode(led2, OUTPUT);
 pinMode(led3, OUTPUT);
 pinMode(led4, OUTPUT);
 pinMode(foto, INPUT);
 pinMode(MISOS, INPUT);      // Configura pines del SPI (no se hace uso del módulo incorporado)
 pinMode(SCKS, OUTPUT);
 pinMode(CSS, OUTPUT);
 digitalWrite(SCKS,0);       // Inicia el reloj deshabilitado.
 digitalWrite(CSS,1);        // Inicia el "Chip Select" en 1.
 digitalWrite(led1,0);
 digitalWrite(led2,0);
 digitalWrite(led3,0);
 digitalWrite(led4,0);
 
 Serial.begin(115200);
 muestra_menu();
}

void loop(){
 numero_funcion = menu_ppal();
 
 switch(numero_funcion){ //Modificar de acuerdo con las funciones que se vayan definiendo.
    case 0:
      analogos_simple();
      break;
    case 1:
      analogos();
      break;
    case 2:
      sensor_temperatura();
      break;
    case 3:
      oscuridad_us();
      break;
    case 4:
      claro_oscuro();
      break;
    case 5:
      claro_oscuro_claro();
      break;
    case 6:
      doble_fotocompuerta();
      break;
    case 99:
      break;
  }
}

 
//FUNCIONES
//-----------------------------------------------
//Menu principal
 
int menu_ppal(){
   int dato_serial;
   int funcion;
   
   while(Serial.available() <= 0); //Espera hasta que llegue un caracter
   dato_serial = Serial.read();
   
   if(dato_serial == 65){//Letra A: sensores análogos pero envía un solo dato. Para usar con interfaz gráfica.
     return 0; 
   }
   
   if(dato_serial == 109){//Letra m: muestra menu.
     muestra_menu();
     return 99;
   }
   
   if(dato_serial == 49){//Caracter 1: sensores análogos.
     Serial.write(dato_serial);
     Serial.println("");
     return 1;
   }
   if(dato_serial == 50){//Caracter 2: sensor de temperatura conectado en puerto SPI.
     Serial.write(dato_serial);
     Serial.println("");
     return 2;
   }
   if(dato_serial == 51){//Caracter 3: tiempo de oscuridad para sensor en puerto D7.
     Serial.write(dato_serial);
     Serial.println("");
     return 3;
   }
   if(dato_serial == 52){//Caracter 4: tiempo de transición claridad<->oscuridad en puerto D7.
     Serial.write(dato_serial);
     Serial.println("");
     return 4;
   }
   if(dato_serial == 53){//Caracter 5: tiempo de transición claridad<->oscuridad en puerto D7.
     Serial.write(dato_serial);
     Serial.println("");
     return 5;
   }
   if(dato_serial == 54){//Caracter 6: tiempo entre sensores conectados a D7 y D8
     Serial.write(dato_serial);
     Serial.println("");
     return 6;
   }
   
   return 99; //Indica que no recibió un caracter valido. A esta funcion se le pueden añadir nuevas opciones cada vez que se cree una función nueva.
}

//----------------------------------------------------------- 
//Función para mostrar el menú.

void muestra_menu(){
   Serial.println("");
   Serial.println("SISTEMA DE ADQUISION DE DATOS PARA EL LABORATORIO INTEGRADO DE FISICA. UNIVERSIDAD DE ANTIOQUIA");
   Serial.println("Ingrese el numero correspondiente a la opcion deseada: ");
   Serial.println("\t 1 : Sensores analogos en los puertos A0, A1, A2, A3.");
   Serial.println("\t 2 : Sensor de temperatura en el puerto SPI.");
   Serial.println("\t 3 : Tiempo de oscuridad para el sensor reflectivo conectado al puerto D7.");
   Serial.println("\t 4 : Tiempos de transicion claridad -> oscuridad para el sensor reflectivo conectado al puerto D7.");
   Serial.println("\t 5 : Tiempos de transicion claridad <-> oscuridad para el sensor reflectivo conectado al puerto D7.");
   Serial.println("\t 6 : Intervalo de tiempo entre los sensores reflectivos conectados a los puertos D7 y D8");
   Serial.print(">");
   return;
}


//----------------------------------------------------------- 
//Función para sensores análogos y de temperatura (Envía solo un dato de cada uno)
void analogos_simple(){
   Serial.print(analogRead(A0));
   Serial.print("\t");
   Serial.print(analogRead(A1));
   Serial.print("\t");
   Serial.print(analogRead(A2));
   Serial.print("\t");
   Serial.print(analogRead(A3));
   Serial.print("\t");
   Serial.println(lee_temp()*0.25);
   return;
}

//-----------------------------------------------------------
//Funcion para sensores análogos
void analogos(){
   int sensor0, sensor1, sensor2, sensor3;
   int serial_dato, tiempo;
   
   Serial.println("");
   Serial.println("\t Ingrese la letra correspondiente al tiempo entre datos:");
   Serial.println("\t \t a: 100ms; b: 500ms; c: 1s; d: 2s");
   Serial.print(">");
   while(Serial.available() <= 0); //Espera hasta que llegue un caracter
   serial_dato = Serial.read();
   switch(serial_dato){
    case 97:
      tiempo=100;
      break;
    case 98:
      tiempo=500;
      break;
    case 99:
      tiempo=1000;
      break;
    case 100:
      tiempo=2000;
      break;
    default:
      Serial.println("Letra no valida. Presione m para volver al menu");
      return;
   }
   Serial.write(serial_dato);
   Serial.println("");
   Serial.print("Eligio un tiempo entre datos de: ");
   Serial.print(tiempo);
   Serial.println(" ms. Presione una tecla para comenzar y otra para terminar.");
   Serial.println("");
   while(Serial.available() <= 0); //Espera hasta que llegue un caracter
   Serial.read(); //Así no se vaya a usar hay que leerlo para vaciar el buffer.
   Serial.println("A0\t A1\t A2\t A3");
   while(Serial.available() <= 0){ //Mientras no llegue ningún caracter
     Serial.print(analogRead(A0));
     Serial.print("\t");
     Serial.print(analogRead(A1));
     Serial.print("\t");
     Serial.print(analogRead(A2));
     Serial.print("\t");
     Serial.println(analogRead(A3));
     delay(tiempo);
   }
   Serial.read(); //Así no se vaya a usar hay que leerlo para vaciar el buffer.
   Serial.println("FIN.");
   Serial.println("Presione el numero correspondiente a la funcion deseada o m para volver al menu.");
   return;
}

//------------------------------------------------------------------------ 
//Funcion para sensor de temperatura conectado en el puerto SPI
void sensor_temperatura(){
   int serial_dato, tiempo;
   
   Serial.println("");
   Serial.println("\t Ingrese la letra correspondiente al tiempo entre datos:");
   Serial.println("\t \t a: 100ms; b: 500ms; c: 1s; d: 2s");
   Serial.print(">");
   while(Serial.available() <= 0); //Espera hasta que llegue un caracter
   serial_dato = Serial.read();
   switch(serial_dato){
    case 97:
      tiempo=100;
      break;
    case 98:
      tiempo=500;
      break;
    case 99:
      tiempo=1000;
      break;
    case 100:
      tiempo=2000;
      break;
    default:
      Serial.println("Letra no valida. Presione m para volver al menu");
      return;
   }
   Serial.write(serial_dato);
   Serial.println("");
   Serial.print("Eligio un tiempo entre datos de: ");
   Serial.print(tiempo);
   Serial.println(" ms. Presione una tecla para comenzar y otra para terminar.");
   Serial.println("");
   while(Serial.available() <= 0); //Espera hasta que llegue un caracter
   Serial.read(); //Así no se vaya a usar hay que leerlo para vaciar el buffer.
   Serial.println("Temperatura");
   while(Serial.available() <= 0){ //Mientras no llegue ningún caracter
     Serial.println(lee_temp()*0.25);
     delay(tiempo);
   }
   Serial.read(); //Así no se vaya a usar hay que leerlo para vaciar el buffer.
   Serial.println("FIN.");
   Serial.println("Presione el numero correspondiente a la funcion deseada o m para volver al menu.");
   return;
}


//----------------------------------------------------------- 
//Función para tiempo de oscuridad
 void oscuridad_us(){  
   
  unsigned long t1, t2, delta_t;

  Serial.println("");
  Serial.println("Presione una tecla para comenzar y otra para terminar.");
  Serial.println("");
  
  while(Serial.available()<=0); //Espera hasta que llegue un caracter
  Serial.read(); //Así no se vaya a usar hay que leerlo para vaciar el buffer.
  Serial.println("Tiempo de oscuridad (us).");
  while(Serial.available()<=0){
   if(digitalRead(foto)==1){ //El sensor reflectivo retorna un estado alto cuando se interrumpe el haz.
     t1 = micros();
     while(digitalRead(foto)==1 && Serial.available()<=0){}
     Serial.println(micros()-t1);
   } 
  }
  Serial.read(); //Así no se vaya a usar hay que leerlo para vaciar el buffer.
  Serial.println("FIN.");
  Serial.println("Presione el numero correspondiente a la funcion deseada o m para volver al menu.");
  return;
}

//------------------------------------------------------------------------------------------------------------------------------------------ 
//Función para tiempos de transición claro->oscuro
//Envia el valor del tiempo transcurrido cada vez que hay una transición claro-oscuro en el sensor reflectivo conectado al puerto D7
void claro_oscuro(){
   
 int flag_start = 0;
 int start_time;
 
 Serial.println("");
 Serial.println("Presione una tecla para comenzar y otra para terminar.");
 Serial.println("");
 
 while(Serial.available()<=0); //Espera hasta que llegue un caracter
 Serial.read(); //Así no se vaya a usar hay que leerlo para vaciar el buffer.
 Serial.println("Tiempos de transicion claro -> oscuro (ms).");
 start_time = millis();
 while(Serial.available()<=0){
   if(digitalRead(foto)==1 && flag_start==0){  //El sensor reflectivo retorna un estado alto cuando se interrumpe el haz.
     Serial.println(millis()-start_time);
     flag_start = 1;
   }
   if(digitalRead(foto)==0){
     flag_start = 0;
   }
 }
 Serial.read(); //Así no se vaya a usar hay que leerlo para vaciar el buffer.
 Serial.println("FIN.");
 Serial.println("Presione el numero correspondiente a la funcion deseada o m para volver al menu.");
 return;
}
 
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//Función para tiempos de transición claro<->oscuro
//Envia el valor del tiempo transcurrido cada vez que hay una transición claro-oscuro u oscuro-claro en el sensor reflectivo conectado al puerto D7.
void claro_oscuro_claro(){
 int foto_actual=0;
 int foto_anterior =1;
 int start_time;
 
 Serial.println("");
 Serial.println("Presione una tecla para comenzar y otra para terminar.");
 Serial.println("");
 
 while(Serial.available()<=0); //Espera hasta que llegue un caracter
 Serial.read(); //Así no se vaya a usar hay que leerlo para vaciar el buffer.
 Serial.println("Tiempos de transicion claro <-> oscuro (ms)");
 start_time = millis();
 
 while(Serial.available()<=0){
   foto_actual=digitalRead(foto);
   if(foto_actual-foto_anterior != 0){  
     Serial.println(millis()-start_time);
   }
   foto_anterior=foto_actual;
 }
 Serial.read(); //Así no se vaya a usar hay que leerlo para vaciar el buffer.
 Serial.println("FIN.");
 Serial.println("Presione el numero correspondiente a la funcion deseada o m para volver al menu.");
 return; 
}
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
//Función para tiempos de transición claro<->oscuro
void doble_fotocompuerta(){
  int t1;
  
  Serial.println("");
  Serial.println("Presione una tecla para comenzar y otra para terminar.");
  Serial.println("");
  
  while(Serial.available()<=0); //Espera hasta que llegue un caracter
  Serial.read(); //Así no se vaya a usar hay que leerlo para vaciar el buffer.
  Serial.println("Tiempo entre sensores reflectivos (ms).");
  while(Serial.available()<=0){
   if(digitalRead(foto)==1){ //El sensor reflectivo conectados a D7 retorna un estado alto cuando se interrumpe el haz.
     t1 = millis();
     while(digitalRead(foto2)==0 && Serial.available()<=0){} //Espera a que se interrumpa el otro sensor reflectivo (D8)
     Serial.println(millis()-t1);
   }else if(digitalRead(foto2)==1){//El sensor reflectivo conectados a D8 retorna un estado alto cuando se interrumpe el haz.
     t1 = millis();
     while(digitalRead(foto)==0 && Serial.available()<=0){} //Espera a que se interrumpa el otro sensor reflectivo (D7)
     Serial.println(millis()-t1);
   }
  }
  Serial.read(); //Así no se vaya a usar hay que leerlo para vaciar el buffer.
  Serial.println("FIN.");
  Serial.println("Presione el numero correspondiente a la funcion deseada o m para volver al menu.");
  return;
}
 
///////////////////////////////////////////FUNCIONES AUXILIARES///////////////////////////////////////////

///// lee_temp(); Ejecuta el protocolo necesario para leer el valor de la temperatura (12bits con incrementos correspondientes a 0.25°C) con el chip MAX6675

int lee_temp(){

int i=0;
int bit_leido;
int dato_actual;
int dato_acumulado=0;
int temperatura;

digitalWrite(CSS,0);
delayMicroseconds(10);

for (i==0; i<16; i++)
  {
    digitalWrite(SCKS,1);
    delayMicroseconds(10); //Se fija SCKS en 50KHz
    bit_leido=digitalRead(MISOS); //Se va construyendo bit a bit el dato de 16 bits arrojado por el chip MAX6675
    dato_actual=bit_leido << (15-i); //Se guarda bit_leido en la posición correspondiente de dato_actual.
    dato_acumulado=dato_actual | dato_acumulado;
    digitalWrite(SCKS,0);
    delayMicroseconds(10); 
  }
digitalWrite(CSS, 1);
delayMicroseconds(10);
temperatura=((dato_acumulado>>3) & 4095); //La temperatura está en los bits 14->3 de dato_acumulado. Temperatura es una variable entre 0 y 4095, que representa incrementos de 0.25°C
return temperatura;
}
