#define _GNU_SOURCE
#include <stdio.h>
#include <sched.h>
#include <stdlib.h>
#include "time.h"
#include <omp.h>
#include "my_cpu_config.h"

#define zero 0.0

long num_step;
double sum = 0.0;
double compute_pi() {
    double delta = 1.0/num_step;
    double x = 0.0f;
    #pragma omp parallel for private(x) reduction(+:sum)
    for(long i=0;i<num_step;i++) {
        x = (i + 0.5) * delta;
        sum += 4.0/(1+x*x)*delta;
    }
    return sum;
}

int main(int argc, char *argv[]) {
    cpu_set_t mask;
    CPU_ZERO(&mask);
    int *team = hybrid_smt;
    int selection = 5;
    int nworkers;
    //printf("nworkers : %d",nworkers);
    if (argc < 3) {
        printf("Program kurang argumen\n");
        printf("Jalankan %s ",argv[0]);
        printf("1 untuk %d performance core\n",nworkers);
        printf("2 untuk %d efficient core\n",nworkers);
        printf("3 untuk %d hybrid core\n",nworkers);
        printf("4 untuk %d performance core smt\n",nworkers);
        printf("tanpa parameter eksekusi pada %d cores berurut\n",nworkers);
        printf("Tambahkan parameter jumlah threads\n");
        //team = hybrid_smt;
    } else
    selection = atoi(argv[1]);
    switch (selection) {
        case 1 : 
                 team = performance_core;
                 break;
        case 2 : team = efficient_core;
                 break;
        case 3 : team = hybrid_core;
                 break;
        case 4 : team = performance_smt;
                 break;
        case 5 : team = performance_smt_pf;
                 break;
        case 6 : team = hybrid_smt;
                 break;
        case 7 : team = hybrid_smt_pf;
                 break;
        default : team = hybrid_smt_pf;
    }
    nworkers = atoi(argv[2]);
    omp_set_num_threads(nworkers);
    for(int i=0;i<nworkers;i++)
         CPU_SET(team[i],&mask);
    int result = sched_setaffinity(0,sizeof(mask),&mask);
    num_step = 2000000000l;
    start_timer();
    compute_pi();
    lap_time("");
 //   printf("\n");
//    printf("Program di eksekusi pada : ");
//    for(int i =0;i<nworkers;i++)
//        printf("cpu %d ",team[i]);
//    printf("\n");
    return 0;
}