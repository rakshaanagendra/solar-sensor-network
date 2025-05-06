//Sensor data logger using C



#include <stdio.h>
#include "sensor.h"
#include "uart.h"

int main(void) {
    sensor_init();  // initializes I2C sensor
    uart_init();    // sets up UART for logging

    while (1) {
        float temperature = read_temperature();
        float humidity = read_humidity();
        
        char buffer[100];
        sprintf(buffer, "Temp: %.2f C, Humidity: %.2f%%\n", temperature, humidity);
        uart_send_string(buffer);
        
        delay_ms(1000); // 1-second delay
    }
    return 0;
}
