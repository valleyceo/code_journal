#include <iostream>

using namespace std;
int pos[45];
int main(){
    int T;
    scanf("%d",&T);
    for(int tc=1;tc<=T;tc++){
        int R,S;
        scanf("%d%d",&R,&S);
        printf("Case #%d: %d\n",tc,(R*(S-1)+1)/2);
        for(int i=0;i<R;i++) pos[i]=R*(S-1)+i;
        if(R%2==0){
            for(int i=0;i<(S-1);i++){
                for(int j=0;j<R/2;j++){
                    printf("%d %d\n",2,pos[j*2+1]-2);
                    for(int k=0;k<j*2+1;k++){
                        pos[k]-=2;
                    }
                    pos[j*2+1]--;
                }
            }
        }
        else{
            if((S-1)%2==0){
                int PP = (S-1)/2;
                for(int i=0;i<PP-1;i++){
                    for(int j=1;j<2*R;j+=2){
                        int cur = j%R;
                        printf("%d %d\n",2,pos[cur]-2);
                        for(int k=0;k<cur;k++){
                            pos[k]-=2;
                        }
                        pos[cur]--;
                    }
                }
                for(int j=1;j<2*R-2;j+=2){
                    int cur = j%R;
                    printf("%d %d\n",2,pos[cur]-2);
                    for(int k=0;k<cur;k++){
                        pos[k]-=2;
                    }
                    pos[cur]--;
                }
                printf("%d %d\n",pos[0],pos[R-1]-pos[0]);
            }
            else{
                int PP = (S-1)/2;
                for(int i=0;i<PP;i++){
                    for(int j=1;j<2*R;j+=2){
                        int cur = j%R;
                        printf("%d %d\n",2,pos[cur]-2);
                        for(int k=0;k<cur;k++){
                            pos[k]-=2;
                        }
                        pos[cur]--;
                    }
                }
                for(int j=1;j<R;j+=2){
                    int cur = j%R;
                    printf("%d %d\n",2,pos[cur]-2);
                    for(int k=0;k<cur;k++){
                        pos[k]-=2;
                    }
                    pos[cur]--;
                }
                printf("%d %d\n",pos[0],pos[R-1]-pos[0]);
            }
        }
    }
}