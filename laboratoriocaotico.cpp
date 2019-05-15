#include <iostream>
# include <cmath>
#include <fstream>
using namespace std; 
const double w0 =1. , gammas =0.2;
const double h =0.1 , delta =1.0;
const double F =1.2 , w =0.2;
const int N =1000;

double g ( double theta0 , double omega0 , double t ) ;
double f ( double theta0 , double omega0 , double t ) ;
int main ( void ) 
{
	ofstream outfile;
	double omega =1;
	double theta =0.1;
	outfile.open("datoscaotico.dat");
	for ( int i =0; i < N ; i ++ )
	{
		outfile<<i*h<<","<<theta<<","<<omega<<endl;
		omega = omega + h * f ( theta , omega , i * h ) ;
		theta = theta + h * g ( theta , omega , i * h ) ;
	}
	outfile.close();
    
    
	theta =0.2;
	outfile.open("datos1caotico.dat");
    for ( int i =0; i < N ; i ++ )
	{
		outfile<<i*h<<","<<theta<<","<<omega<<endl;
		omega = omega + h * f ( theta , omega , i * h ) ;
		theta = theta + h * g ( theta , omega , i * h ) ;
	}
	outfile.close();
    
    theta =0.3;
	outfile.open("datos2caotico.dat");
    for ( int i =0; i < N ; i ++ )
	{
		outfile<<i*h<<","<<theta<<","<<omega<<endl;
		omega = omega + h * f ( theta , omega , i * h ) ;
		theta = theta + h * g ( theta , omega , i * h ) ;
	}
	outfile.close();
    
    theta =0.4;
	outfile.open("datos3caotico.dat");
    for ( int i =0; i < N ; i ++ )
	{
		outfile<<i*h<<","<<theta<<","<<omega<<endl;
		omega = omega + h * f ( theta , omega , i * h ) ;
		theta = theta + h * g ( theta , omega , i * h ) ;
	}
	outfile.close();
    
    
	return 0;
}
double g ( double theta0 , double omega0 , double t ) 
{
	return omega0 ;
}
double f ( double theta0 , double omega0 , double t ) 
{
	return - w0 * w0 * sin ( theta0 ) - gammas * omega0 + F * sin ( w * t + delta ) ;
}
