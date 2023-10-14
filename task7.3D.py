# Importing the sleep function from the time module
from time import sleep

# Importing DistanceSensor and PWMLED classes from the gpiozero library
from gpiozero import DistanceSensor, PWMLED

# Create a PWM LED on GPIO pin 13
led = PWMLED(13)

# Create a distance sensor with echo on GPIO 18 and trigger on GPIO 17
distance_sensor = DistanceSensor(echo=18, trigger=17)

# Define a safe_exit function to handle termination signals
def exit_safely():
    exit(1)

# Main function to control the LED brightness based on distance
def main():
    # A flag to indicate if the program is running
    running = True
    
    try:
        # Turn on the LED initially
        led.on()
        
        while running:
            # Get the distance from the sensor
            distance = distance_sensor.value
            
            # Print the distance with two decimal places
            print(f'Distance: {distance:1.2f} meters')
            
            # Calculate the duty cycle for LED brightness
            brightness = round(1.0 - distance, 1)
            
            # Ensure the brightness is not below 0
            if brightness < 0:
                brightness = 0.0
            
            # Set the LED brightness
            led.value = brightness
            
            # Sleep for a short duration (0.1 seconds)
            sleep(0.1)
    
    except KeyboardInterrupt:
        pass
    
    finally:
        # Clean up and close the sensor when the program ends
        running = False
        distance_sensor.close()

# Check if this script is being run directly
if __name__ == '__main__':
    main()
