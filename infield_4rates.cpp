#include <iostream>
#include <cmath>
#include <random>
#include <stdio.h>
using namespace std;

#define PRINTER(name) std::cout << "#" << #name << " = " << name << std::endl;

int movetest(double dt, double *k, double rand){
	if (rand < k[0]*dt){
		return 0;
	} else if (rand < (k[0]+k[1])*dt){
		return 1;
	} else if (rand < (k[0]+k[1]+k[2])*dt ){
		return 2;
	} else if (rand < (k[0]+k[1]+k[2]+k[3])*dt ){
		return 3;
	} else {
		return 5;
	}
}

int fliptest(double mu,int sigma, double rand,int rand2){
	if (rand < 1-mu){
		return sigma;
	} else {
		return sigma = (sigma + rand2) % 4;
	}
}

void lefthook(int move, int *x, int *y, int *count, int nx, int nxh, int nx1, int nx2, int ny, int nyh){
	if (move == 0){
		(*x)++;
		if ((*x) == (nx+1) && (*y) <= nyh){
			cout << *x;
			(*x)--;
		}else if ((*x) == (nx+1)){
			(*count)++;
			(*x)=2;
		}
	} else if (move == 1){
		(*x)--;
		if ((*x) == 0 && (*y) <= nyh){
			(*x)++;
		}else if ((*x) == 0){
			(*x) = nx-1;
			(*count)--;
		}
	} else if (move == 2){
		(*y)++;
		if ((*x) <= nxh && (*y) == (nyh+1)){
			(*y)--;
		} else if ((*y) == (ny+1)){
			(*y) = ny;
		}
	} else if (move == 3){
		(*y)--;
		if ((*x) <= nxh && (*y) == nyh){
			(*y)++;
		}else if ((*y) == 0){
			(*y) = 1;
		}
	}
}


void righthook(int move, int *x, int *y, int *count, int nx, int nxh, int nx1, int nx2, int ny, int nyh){
	if (move == 0){
		(*x)++;
		if ((*x) == (nx+1) && (*y) <= nyh){
			(*x)--;
		}else if ((*x) == (nx+1)){
			(*count)++;
			(*x)=2;
		}
	} else if (move == 1){
		(*x)--;
		if ((*x) == 0 && (*y) <= nyh){
			(*x)++;
		}else if ((*x) == 0){
			(*x) = nx -1;
			(*count)--;
		}
	} else if (move == 2){
		(*y)++;
		if ((*x) >= nxh && (*y) == (nyh+1)){
			(*y)--;
		} else if ((*y) == (ny+1)){
			(*y) = ny;
		}
	} else if (move == 3){
		(*y)--;
		if ((*x) >= nxh && (*y) == nyh){
			(*y)++;
		}else if ((*y) == 0){
			(*y) = 1;
		}
	}
}
void symhook(int move, int *x, int *y, int *count, int nx, int nxh, int nx1, int nx2, int ny, int nyh){
	if (move == 0){
		(*x)++;
		if ((*x) == (nxh)+1 && (*y) <= nyh){
			(*x)--;
		}else if ((*x) == (nx+1)){
			(*count)++;
			(*x)=2;
		}
	} else if (move == 1){
		(*x)--;
		if ((*x) == nxh && (*y) <= nyh){
			(*x)++;
		}else if ((*x) == 0){
			(*x) = nx -1;
			(*count)--;
		}
	} else if (move == 2){
		(*y)++;
		if ((*x) >= nx1 && (*x) <= nx2 && (*y) == (nyh+1)){
			(*y)--;
		} else if ((*y) == (ny+1)){
			(*y) = ny;
		}
	} else if (move == 3){
		(*y)--;
		if ((*x) >= nx1 && (*x) <= nx2 && (*y) == (nyh)){
			(*y)++;
		}else if ((*y) == 0){
			(*y) = 1;
		}
	}
}
void no_obstacle(int move, int *x, int *y, int *count, int nx, int nxh, int nx1, int nx2, int ny, int nyh){
	if (move == 0){
		(*x)++;
		if ((*x) == (nx+1)){
			(*count)++;
			(*x)=2;
		}
	} else if (move == 1){
		(*x)--;
		if ((*x) == 0){
			(*x) = nx -1;
			(*count)--;
		}
	} else if (move == 2){
		(*y)++;
		if ((*y) == (ny+1)){
			(*y) = ny;
		}
	} else if (move == 3){
		(*y)--;
		if ((*y) == 0){
			(*y) = 1;
		}
	}
}
int testerror (double dt, double p[],double m[],double u[],double d[]){
	if ( (p[1]+p[2]+p[3]+p[0])*dt > 1 | (m[1]+m[2]+m[3]+m[0])*dt > 1 | (u[1]+u[2]+u[3]+u[0])*dt > 1 | (d[1]+d[2]+d[3]+d[0])*dt > 1){
		cerr << "Error: rates to high for dt" << endl;
		exit(1);
	}
	return 1;
}

int main(int argc, char *argv[]){
    const double pi2 = 6.28318530718;
	const double lx = 1;
	const double ly = 1;
	const double dx = 0.1;
	const double dy = 0.1;
	/* const int nx = int(lx/dx); */
	/* const int ny = int(ly/dx); */
	const int nx = 10;
	const int ny = 10;
	const int nx1 = 2;
	const int nx2 = 8;
	const int nxh = 5;
	const int nyh = 5;
    const int N = 2000; 
	double rand = 0;
	int rand2 = 0;

    /* init */
	
	std::random_device dev;
	std::mt19937 rng(dev());
	std::uniform_real_distribution<double> dist(0,1);
	std::uniform_int_distribution<int> distsigma(0,3);
	std::uniform_int_distribution<int> distx(1,nx);
	std::uniform_int_distribution<int> disty(1,ny);
   
	int x = 0;
    int y = 0;
	int sigma = distsigma(rng);
	int count = 0;
	int move = 0;	

	double c = stod(argv[1]);
	double a = stod(argv[2]);
	double dt = stod(argv[3]);
	double tmax = stod(argv[4]);

	int obstacle = stod(argv[5]);
	void (*movefunc)(int move, int *x, int *y, int *count, int nx, int nxh, int nx1, int nx2, int ny, int nyh);
	
	if (obstacle == 1){
		movefunc=&lefthook;
	} else if (obstacle == 2) {
		movefunc=&righthook;
	} else if (obstacle == 3) {
		movefunc=&symhook;
	} else {
		movefunc=&no_obstacle;
	}

	PRINTER(dt);
	PRINTER(a);
	PRINTER(c);
	PRINTER(N);
	PRINTER(tmax);

	for (double e = -2; e <= 2; e+=0.2){

		double bp = 0.5*(c+e);
		double bm = 0.5*(-c+e);
		double bu = 0.5*(c);
		double bd = 0.5*(-c);
		double be = 0.5*(e);
		
		double p[4] = {(bp+sqrt(bp*bp+1))/dx,1/((bp+sqrt(bp*bp+1))*dx),1/dx,1/dx};
		double m[4] = {(bm+sqrt(bm*bm+1))/dx,1/((bm+sqrt(bm*bm+1))*dx),1/((bu+sqrt(bu*bu+1))*dx),1/((bu+sqrt(bu*bu+1))*dx)};
		double u[4] = {(be+sqrt(be*be+1))/dx,1/((be+sqrt(be*be+1))*dx),(bu+sqrt(bu*bu+1))/dx,1/((bu+sqrt(bu*bu+1))*dx)};
		double d[4] = {(be+sqrt(be*be+1))/dx,1/((be+sqrt(be*be+1))*dx),(bd+sqrt(bd*bd+1))/dx,1/((bd+sqrt(bd*bd+1))*dx)};
		double *list_of_rates[4] = {p, m, u, d};
		double *rates;
		testerror(dt,p,m,u,d);
		count = 0;
		for (int i=1; i <= N; i++){
			x = distx(rng);
			y = disty(rng);
			for (double t = 0; t < tmax; t += dt){
				rand = dist(rng);
				rand2 = distsigma(rng);
				sigma = fliptest(a*dt,sigma,rand,rand2);

				rates = list_of_rates[sigma];

				rand = dist(rng);
				move = movetest(dt,rates,rand);
				movefunc(move,&x,&y,&count,nx,nxh,nx1,nx2,ny,nyh);
				/* cout << x << ";" << y << endl; */
				/* cout << count << endl; */
			}
		}
		cout << e << ";" << count/(tmax) << endl;
	}
	return 0;
}
