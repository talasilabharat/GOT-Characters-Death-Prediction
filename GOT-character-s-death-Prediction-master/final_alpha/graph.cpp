// c libraries
#include <cmath>
#include <climits>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <cassert>

//data structure
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <string.h>
#include <set>
#include <map>

//other important stl
#include <iostream>
#include <algorithm>
#include <string>
#include <functional>
#include <utility>
#include <iterator>

using namespace std;

#define tr(x,it) for(auto it=begin(x);it!=end(x);it++ )
#define loop(a,b,i) for(int i=a;i<b;i++)
#define rloop(a,b,i) for(int i=b-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define fi first 
#define se second 

typedef vector<int> vint;
typedef pair<double,int> pint;
typedef vector<pint> vpint;

#define LIMT 2000
#define YR 300
int n,e;
double score[LIMT];
int death[LIMT];
int year[LIMT];
bool *visit;	

vpint *a;
double alpha=0.5;

void bfs(int start){
	int dis=1;
	visit=new bool[LIMT];
	fill_n(visit,LIMT,false);
	queue<pint> q;
	q.push(mp(0,start));
	visit[start]=true;
	int curr_child=1;
	int next_child=0;
	while(!q.empty()){
		pint f=q.front();
		q.pop();
		curr_child--;
		int w=f.fi;
		int u=f.se;
		for(vpint::iterator it=a[u].begin();it!=a[u].end();it++){
			if(!visit[it->se]){
				q.push( mp(it->fi,it->se) );
				next_child++;
				score[it->se]=score[it->se]+((double)alpha/pow(3,dis))*(double)it->fi;
				visit[it->se]=true;
			}
		}
		if(curr_child==0){
			dis++;
			curr_child=next_child;
			next_child=0;
		}
		if(dis==5){
			break;
		}
	}
}

void addEdge(int u,int v,double w){
	a[u].pb( mp(w,v) );
	a[v].pb( mp(w,u) );
}

int main() {
	// your code goes here
	n=1946;
	ifstream graph;
	graph.open("input");
	ifstream death_in;
	death_in.open("character-isAlive");
	ifstream year_in;
	year_in.open("character-year");
	cout<<"Reading the graph:"<<endl;
	a=new vpint[LIMT];
	fill_n(score,LIMT,0);
	fill_n(death,LIMT,0);
	fill_n(year,LIMT,0);
	char str[255];
	graph.getline(str,255);
	while(str[0]!='\0'){		
		char * pch;
		pch = strtok (str,",");
		int u=stoi(pch);
		pch = strtok (NULL, ",");	
		int v=stoi(pch);
		pch = strtok (NULL, ",");
		double w=stod(pch);
		graph.getline(str,255);
		addEdge(u,v,w);
	}
	cout<<"Graph reading done"<<endl;
	loop(0,n,i){
		death_in>>death[i+1];
	}
	loop(0,n,i){
		year_in>>year[i+1];
	}
	loop(1,n+1,i){
		if(death[i]==0 && year[i]<YR){
			bfs(i);	
		} 
	}
	ofstream score_out;
	score_out.open("score");
	pint output[LIMT];
	double avg=0;
	loop(1,n+1,i){
		if(a[i].size()!=0){
			output[i].fi=score[i]/a[i].size();
			output[i].se=i;
		}
		else{
			output[i].fi=score[i];
			output[i].se=i;
		}
	}
	loop(1,n+1,i){
		avg+=output[i].fi;
	}
	avg=avg/n;
	sort(output,output+LIMT,greater<pint>());
	int correct=0;
	int wrong=0;
	loop(0,LIMT,i){
		if(death[output[i].se]==0 && output[i].fi>avg && year[output[i].se]>=YR){
			correct++;
			score_out<<output[i].se<<" _/ "<<output[i].fi<<" "<<death[output[i].se]<<endl;
		}
		else if(output[i].fi<=avg && year[output[i].se]>=YR){
			wrong++;
			score_out<<output[i].se<<" X "<<output[i].fi<<" "<<death[output[i].se]<<endl;
		}
		else if(year[output[i].se]==0 && output[i].fi>avg){
			score_out<<output[i].se<<" P "<<output[i].fi<<" "<<death[output[i].se]<<endl;
		}
	}
	double acc=correct*100/(wrong+correct);
	cout<<"accuracy is :"<<acc<<endl;
	return 0;
}
