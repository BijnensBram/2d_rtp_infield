#include <iostream>
#include <cmath>
#include <random>
#include <stdio.h>
using namespace std;

#define PRINTER(name) std::cout << "#" << #name << " = " << name << std::endl;

int movetest(double dt, double k, double rand){
	if (rand < k*dt){
		return 0;
	} else if (rand < 2*k*dt){
		return 1;
	} else if (rand < 3*k*dt ){
		return 2;
	} else if (rand < k*4*dt ){
		return 3;
	} else {
		return 5;
	}
}

int testerror (double dt, double k){
	if ( 4*k*dt > 1 ){
		cerr << "Error: rates to high for dt" << endl;
		exit(1);
	}
	return 1;
}

int main(int argc, char *argv[]){
    const double pi2 = 6.28318530718;
	const double tmax = 2000;
	const double lx = 1;
	const double ly = 1;
	const double dx = 0.1;
	const double dy = 0.1;
	/* const int nx = int(lx/dx); */
	/* const int ny = int(ly/dx); */
	const int nx = 4;
	const int ny = 4;
    const int N = 100; 
	double rand = 0;
	double rand2 = 0;

    /* init */
    int x = 0;
    int y = 0;
	/* int sigma = 1; */

    /* sim */
	std::random_device dev;
	std::mt19937 rng(dev());
	std::uniform_real_distribution<double> dist(0,1);
	double c = stod(argv[1]);
	double a = stod(argv[2]);
	double dt = stod(argv[3]);
	
	double k = c*c*0.5/a;
	testerror(dt,k);
	PRINTER(dt);
	PRINTER(a);
	PRINTER(c);
	PRINTER(N);
	PRINTER(tmax);

	for (double e = 0; e <= 2; e+=0.1){

		int move = 0;	
		int count = 0;
		for (int i=1; i <= N; i++){
			rand = dist(rng);
			x = int(rand*nx);
			rand = dist(rng);
			y = int(rand*ny);
			for (double t = 0; t < tmax; t += dt){
				rand = dist(rng);
				move = movetest(dt,k,rand);
				if (move == 0){
					x++;
					if (x == nx + 1 && y <= int(nx*0.5)){
						x = nx;
					} else if (x == nx+1){
						count++;
						x=1;
					}
				} else if (move == 1){
					x--;
					if (x == -1 && y <= int(ny*0.5)){
						x = 0;
					} else if (x == -1){
						x = nx -1;
						count--;
					}
				} else if (move == 2){
					y++;
					if (y == ny+1){
						y = ny;
					} else if (x >= int(0.5*nx) && y == int(0.5*ny)+1){
						y--;
					}
				} else if (move == 3){
					y --;
					if (y == -1){
						y = 0;
					} else if (x >= int(0.5*nx) && y == int(0.5*ny)){
						y++;
					}
				}
				/* cout << x << ";" << y << endl; */
			}
		}
		cout << e << ";" << count/(tmax*N) << endl;
	}
	return 0;
}
