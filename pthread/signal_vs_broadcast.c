#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#define N_THREADS 3
#define TCOUNT 10
#define COUNT_LIMIT 100

int     count = 0;
pthread_mutex_t count_mutex;
pthread_cond_t count_cv;

void* inc_count1(void* t){
    pthread_t thread_id=pthread_self();
    size_t i;
    sleep(1); // make sure the other two threads acquired the lock and blocked at pthread_cond_wait
    pthread_mutex_lock(&count_mutex);
    for(i=0;i<5;i++){
        count++;
        sleep(1);
        printf("thread_id: %lu, inc_count1, count: %d\n",thread_id,count);
    }
    pthread_cond_signal(&count_cv);
    // pthread_cond_broadcast(&count_cv);
    pthread_mutex_unlock(&count_mutex);
    pthread_exit(NULL);

}
void *inc_count2(void *t) 
{
  pthread_t thread_id=pthread_self();
  size_t i=0;
  for(i=0;i<5;i++){
    pthread_mutex_lock(&count_mutex);
    while(count<5){
        pthread_cond_wait(&count_cv,&count_mutex);
    }
    count++;
    printf("thread: %ld, inc_count2, count: %d\n",thread_id,count);
    sleep(1);
    pthread_mutex_unlock(&count_mutex);
  }

  pthread_exit(NULL);
}


int main()
{
  int i, rc; 
  pthread_t threads[N_THREADS];

  /* Initialize mutex and condition variable objects */
  pthread_mutex_init(&count_mutex, NULL);
  pthread_cond_init (&count_cv, NULL);

  /* For portability, explicitly create threads in a joinable state */
  rc=pthread_create(&threads[0], NULL, inc_count1, NULL);
  if(rc){
      fprintf(stderr,"pthread_create, rc: %d\n",rc);
  }
  pthread_create(&threads[1], NULL, inc_count2, NULL);
  if(rc){
      fprintf(stderr,"pthread_create, rc: %d\n",rc);
  }
  pthread_create(&threads[2],NULL,inc_count2,NULL);
  /* Wait for all threads to complete */
  for (i = 0; i < N_THREADS; i++) {
    rc=pthread_join(threads[i], NULL);
    if(rc){
        fprintf(stderr,"pthread_join, thread: %ld, rc: %d\n",threads[i],rc);
    } else {
        printf("pthread_join, thread: %ld, rc: %d\n",threads[i],rc);
    }
  }

  /* Clean up and exit */
  pthread_mutex_destroy(&count_mutex);
  pthread_cond_destroy(&count_cv);
  pthread_exit (NULL);

}
