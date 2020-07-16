#LED 하나는 점점 밝아지고, 하나는 점점 어두워지게
import RPi.GPIO as GPIO
  import time
  ​
  GPIO.setmode(GPIO.BCM)
  ​
  led_pin1 = 14
  led_pin2 = 15
  ​
  GPIO.setup(led_pin1, GPIO.OUT)
  GPIO.setup(led_pin2, GPIO.OUT)
  ​
  def setLight(light, p):
      p.ChangeDutyCycle(light)
      
  try:
      p1 = GPIO.PWM(led_pin1, 100)
      p2 = GPIO.PWM(led_pin2, 100)
      p1.start(0)
      p2.start(0)
  ​
      while True :
          # 첫번째 LED 점점 밝아지게
          for i in range(10):
              GPIO.output(led_pin1, True)
              p1.ChangeDutyCycle(i*10)
              setLight(i * 10, p1)
              time.sleep(0.5)
              
           # 두번째 LED 점점 어두워지게
          for j in range(10, -1, -1):
              p2.start(100)
              GPIO.output(led_pin2, True)
              p2.ChangeDutyCycle(j*10)
              setLight(j * 10, p2)
              time.sleep(0.5)  
          
  except KeyboardInterrupt:
      pass
  finally:
      GPIO.cleanup()
   

#led 밝기 조절
import RPi.GPIO as GPIO
import time
  ​
  GPIO.setmode(GPIO.BCM)
  ​
  led_pin1 = 14
  led_pin2 = 15
  ​
  GPIO.setup(led_pin1, GPIO.OUT)
  GPIO.setup(led_pin2, GPIO.OUT)
  ​
  ##단계(1~10)를 넣어 LED 밝기를 조절
  def setLight(light, p):
      p.ChangeDutyCycle(light*10)
  ​
  try:
      p = GPIO.PWM(led_pin1, 100)
      p.start(0)
      
      while True :
          for i in range(10):
              GPIO.output(led_pin1, True)
              GPIO.output(led_pin2, False)
              p.ChangeDutyCycle(i*10)
              setLight(i, p)
              time.sleep(1)
            
  except KeyboardInterrupt:
      pass
  finally:
      GPIO.cleanup()
      
      
# 모터 PWM
import RPi.GPIO as GPIO
  import time
  ​
  GPIO.setmode(GPIO.BCM)
  ​
  GPIO_RP = 4
  GPIO_RN = 25
  GPIO_EN = 12
  ​
  GPIO.setup(GPIO_RP, GPIO.OUT) # IN1
  GPIO.setup(GPIO_RN, GPIO.OUT) # IN2
  GPIO.setup(GPIO_EN, GPIO.OUT) # PWM
  ​
  ##단계(1~10)를 넣어 모터의 속도를 조절
  def setSpeed(speed,p):
      p.ChangeDutyCycle(speed*10)
      
  try:
      p = GPIO.PWM(GPIO_EN, 100) # 100hz
      p.start(0) # start the PWM on 0% duty cycle  
      
      while True:
          for i in range(10):
              GPIO.output(GPIO_RP, True)
              GPIO.output(GPIO_RN, False)
              setSpeed(i, p)            
              time.sleep(1)
  finally:    
      GPIO.cleanup()



