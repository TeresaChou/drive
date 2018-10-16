#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <linux/i2c-dev.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <unistd.h>

// The arduino board i2c address (slave)
#define ADDRESS 0x53
// The I2C bus: This is for V2 pi's. For V1 Model B you need i2c-0
static const char *devName = "/dev/i2c-1";

int main(int argc, char** argv) {
	int file, num;
	printf("I2C: Connecting\n");
	if ((file = open(devName, O_RDWR)) < 0) {
		fprintf(stderr, "I2C: Failed to access %d\n", devName);
		exit(1);
	}
	printf("I2C: acquiring buss to 0x%x\n", ADDRESS);
	if (ioctl(file, I2C_SLAVE, ADDRESS) < 0) {
		fprintf(stderr, "I2C: Failed to acquire bus access/talk to slave 0x%x\n", ADDRESS);
		exit(1);
	}

	while (1) {
		usleep(1000000);
		char buf[7];
		buf[0] = 0x32;
		if (read(file, buf, 6) == 6) {
			float x, y, z;
			float mult = 0.004;
			x = mult * ((buf[1] << 8) | buf[0]);
			y = mult * ((buf[3] << 8) | buf[2]);
			z = mult * ((buf[5] << 8) | buf[4]);
			printf("x: %f, y: %f, z: %f\n", x, y, z);
		}
	}
}

