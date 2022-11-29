#define _GNU_SOURCE
#include <stdio.h>
#include <cilk/cilk.h>
#include <cilk/cilkscale.h>
#include <sched.h>
#include <stdlib.h>
#include "time.h"
#include "my_cpu_config.h"

#define zero 0.0

long num_step;
void zero_double(void *view) { *(double *)view = 0.0; }
void add_double(void *left, void *right)
    { *(double *)left += *(double *)right; }
double cilk_reducer(zero_double, add_double) sum;

double compute_pi() {
    double cilk_reducer(zero_double,add_double) sum = 0.0;
    double delta = 1.0/num_step;
    cilk_for(long i=0;i<num_step;i++) {
        double x = (i + 0.5) * delta;
        sum += 4.0/(1+x*x)*delta;
    }
    return sum;

}

int main(int argc, char *argv[]) {
    cpu_set_t mask;
    CPU_ZERO(&mask);
    int *team = hybrid_smt;
    int selection = 5;
    int nworkers = atoi(getenv("CILK_NWORKERS"));
    if (argc < 2) {
        printf("Program kurang argumen\n");
        printf("Jalankan %s ",argv[0]);
        printf("1 untuk %d performance core\n",nworkers);
        printf("2 untuk %d efficient core\n",nworkers);
        printf("3 untuk %d hybrid core\n",nworkers);
        printf("4 untuk %d performance core smt\n",nworkers);
        printf("tanpa parameter eksekusi pada %d cores berurut\n",nworkers);
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
        default : team = hybrid_smt;
    }
    for(int i=0;i<nworkers;i++)
         CPU_SET(team[i],&mask);
    int result = sched_setaffinity(0,sizeof(mask),&mask);
    num_step = 2000000000l;
    printf("%d,",nworkers);
    start_timer();
//   wsp_t start = wsp_getworkspan();
//    printf("pi estimation : %f\n",compute_pi());
    compute_pi();
    lap_time("");
//    wsp_t end = wsp_getworkspan();
//    wsp_t elapsed = wsp_sub(end,start);
//    wsp_dump(elapsed,"pi_sample");
//    printf("\n");
//    printf("Program di eksekusi pada : ");
//    for(int i =0;i<nworkers;i++)
//        printf("cpu %d ",team[i]);
    //printf("\n");
    return 0;
}