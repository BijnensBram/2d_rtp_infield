#include <iostream>
#include <cmath>
#include <random>
#include <stdio.h>
using namespace std;

#define PRINTER(name) std::cout << "#" << #name << " = " << name << std::endl;

void printer(char *name, int value) {
    printf("name: %s\tvalue: %d\n", name, value);
}

bool inRange(unsigned low, unsigned high, unsigned x)
{
return (low <= x && x <= high);
}

int initialise(int n){
	std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<int> dist(0,n);
    return dist(rng);
}

int initsigma(){
	std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<int> dist(1,4);
    return dist(rng);
}

int update(int rho[],int nrho[],int nx){
    for (int i = 0; i <= nx ; i++){
        rho[i] = nrho[i];
    }
    return 0;
}

int movetest(double dt, double kf, double kb, double rand){
	std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_real_distribution<double> dist(0,1);
	rand = dist(rng);

	if (rand < kf*dt){
		return 1;
	} else if (rand < (kf+kb)*dt){
		return -1;
	} else {
		return 0;
	}
}

int fliptest(double mu,int sigma, double rand){
	std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_real_distribution<double> dist(0,1);
	rand = dist(rng);

	if (rand > mu){
		return sigma;
	} else {
		if (sigma == 1){
			rand = dist(rng);
			if (rand < 0.333333333) {
				return 2;
			} else if (rand < 0.666666666) {
				return 3;
			} else {
				return 4;
			}
		} else if (sigma == 2){
			rand = dist(rng);
			if (rand < 0.333333333) {
				return 1;
			} else if (rand < 0.666666666) {
				return 3;
			} else {
				return 4;
			}
		} else if (sigma == 3){
			rand = dist(rng);
			if (rand < 0.333333333) {
				return 1;
			} else if (rand < 0.666666666) {
				return 2;
			} else {
				return 4;
			}
		} else {
			rand = dist(rng);
			if (rand < 0.333333333) {
				return 1;
			} else if (rand < 0.666666666) {
				return 2;
			} else {
				return 3;
			}
		}
	}
}

int testerror (double dt, double kpf,double kpb, double kmf, double kmb,double kuf,double kub, double kdf,double kdb){
	if (dt*(kpf+kpb) > 1 | dt*(kmb+kmf) > 1 | dt*(kuf+kub) > 1 | dt*(kdb+kdf) > 1){
		cerr << "Error: rates to high for dt" << endl;
		exit(1);
	}
	return 1;
}

int main(int argc, char *argv[]){
    const double pi2 = 6.28318530718;
	const double tmax = 10;
	const double lx = 3;
	const double ly = 1;
	const double dx = 0.02;
	const double dy = 0.02;
	const int nx = int(lx/dx);
	const int ny = int(ly/dx);
    const int N = 100; 
	double rand = 0;

    /* init */
    int x = 0;
    int y = 0;
	int sigma = initsigma();
	/* int sigma = 1; */

    /* sim */
	double c = stod(argv[1]);
	double a = stod(argv[2]);
	double dt = stod(argv[3]);
	
	for (double e = 0; e < 10; e+=0.25){

		double bp = 0.5*(c+e);
		double bm = 0.5*(-c+e);
		double bu = 0.5*(c);
		double bd = 0.5*(-c);

		double kpf = (bp+sqrt(bp*bp+1))/dx;
		double kpb = 1/((bp+sqrt(bp*bp+1))*dx);

		double kmf = (bm+sqrt(bm*bm+1))/dx;
		double kmb = 1/((bm+sqrt(bm*bm+1))*dx);
		
		double kuf = (bu+sqrt(bu*bu+1))/dx;
		double kub = 1/((bu+sqrt(bu*bu+1))*dx);

		double kdf = (bd+sqrt(bd*bd+1))/dx;
		double kdb = 1/((bd+sqrt(bd*bd+1))*dx);
		int move = 0;	



		/* PRINTER(dt); */
		/* PRINTER(dx); */
		/* PRINTER(a); */
		/* PRINTER(kpf); */
		/* PRINTER(kpb); */
		/* PRINTER(kmf); */
		/* PRINTER(kmb); */
		/* PRINTER(kuf); */
		/* PRINTER(kub); */
		/* PRINTER(kdf); */
		/* PRINTER(kdb); */
		
		testerror(dt,kpf,kpb,kmf,kmb,kuf,kub,kdf,kdb);
		int count = 0;
		for (int i=1; i <= N; i++){
			x = initialise(nx);
			y = initialise(ny);
			for (double t = 0; t < tmax; t += dt){
				sigma = fliptest(a*dt,sigma,rand);
				if (sigma == 1){
					move = movetest(dt,kpf,kpb,rand);
					x+=move;

					if (y <= int(ny/2) && x == int(2*nx/3)){
						if (move == 1){
							x -= move;
						}
					} else if (y <= int(ny/2) && x == int(2*nx/3)+1){
						if (move == -1){
							x -= move;
						}
					} else if (x == nx+1){
						x = 1;
						count++;
					} else if (x == -1){
						x = nx-1;
						count--;
					}
				} else if (sigma == 2){
					move = movetest(dt,kmf,kmb,rand);
					x += move;
					if (y <= int(ny/2) && x == int(2*nx/3)){
						if (move == 1){
							x -= move;
						}
					} else if (y <= int(ny/2) && x == int(2*nx/3)+1){
						if (move == -1){
							x -= move;
						}
					} else if (x == nx+1){
						x = 1;
						count++;
					} else if (x == -1){
						x = nx-1;
						count--;
					}
				} else if (sigma == 3){
					move = movetest(dt,kuf,kub,rand);
					y+=move;
					if (y == int(ny/2) && x <= 2*nx/3 && x >= nx/3){
						if (move == 1){
							y -= move;
						}
					} else if (y == int(ny/2)+1 && x <= 2*nx/3 && x >= nx/3){
						if (move == -1){
							y -= move;
						}
					} else if (y == ny+1){
						y = ny;
					} else if (y == -1){
						y = 0;
					}
				} else {
					move = movetest(dt,kdf,kdb,rand);
					y+=move;
					if (y == int(ny/2) && x <= 2*nx/3 && x >= nx/3){
						if (move == 1){
							y -= move;
						}
					} else if (y == int(ny/2)+1 && x <= 2*nx/3 && x >= nx/3){
						if (move == -1){
							y -= move;
						}
					} else if (y == ny+1){
						y = ny;
					} else if (y == -1){
						y = 0;
					}
				}
				/* cout << x << ";" << y << endl; */
				/* cout << sigma << endl; */
			}
		}
		cout << e << ";" << count/(tmax*N) << endl;
	}
	return 0;
}
