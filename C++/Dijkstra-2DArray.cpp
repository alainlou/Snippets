#include <bits/stdc++.h>
using namespace std;

int minDistance(int distances[], bool subSet[], int n){
	int min = INT_MAX, min_index;
	
	for(int i = 0; i < n; i++){
		if(subSet[i] == false && distances[i] <= min){
			min = distances[i], min_index = i;
		}
	}
	
	return min_index;
}

int main(){
	//processing
	int n, m;
	cin >> n >> m;
	
	int graph[n][n];

	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			if(i == j){
				graph[i][j] = 0;
			}
			else{
				graph[i][j] = INT_MAX;
			}
		}
	}
	
	int srcNode = 0;
	
	for(int i = 0; i < m; i++){
		int a,b,c;
		cin >> a >> b >> c;
		//0-indexed
		a--;
		b--;
		graph[a][b] = min(c, graph[a][b]);
		graph[b][a] = min(c, graph[a][b]);
	}
	
	//dijkstra's
	int distances[n];	
	
	bool subSet[n];
	
	for(int i = 0; i < n; i++){
		distances[i] = INT_MAX, subSet[i] = false;
	}
	
	distances[srcNode] = 0;
	
	for(int j = 0; j < n-1; j++){
		int u = minDistance(distances, subSet, n);
		subSet[u] = true;
		for(int k = 0; k < n; k++){
			if(!subSet[k] && graph[u][k] != INT_MAX && distances[u] != INT_MAX && distances[u]+graph[u][k] < distances[k]){
				distances[k] = distances[u] + graph[u][k];
			}
		}
	}
	
	for(int k = 0; k < n; k++){
		if(distances[k] != INT_MAX){
			cout << distances[k] << "\n";
		}
		else{
			cout << -1 << "\n";
		}
	}
	
	return 0;
}

