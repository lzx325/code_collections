import os
import time
from mpi4py import MPI
if __name__=="__main__":
    comm = MPI.COMM_WORLD
    my_rank = comm.Get_rank()
    num_procs = comm.Get_size()

    SLURM_NTASKS=os.environ["SLURM_NTASKS"]
    SLURM_PROCID=os.environ["SLURM_PROCID"]

    processor_name=MPI.Get_processor_name()

    if my_rank == 0:
        print("This is process 0 (name: %s). We have %d processes."%(processor_name, num_procs))
        for other_rank in range(1,num_procs):
            comm.send(
                obj="Hello %d"%(other_rank),
                dest=other_rank,
                tag=0
            )
        
        for other_rank in range(1,num_procs):
            data = comm.recv(
                source=other_rank,
                tag=0
            )
            print(data)
    else:
        data = comm.recv(
            source=0,
            tag=0
        )
        assert data.startswith("Hello ")
        comm.send(
            obj="Process %d (name: %s) reporting for duty."%(my_rank,processor_name),
            dest=0,
            tag=0
        )
    print("Process %d going to sleep"%(my_rank))
    time.sleep(20)
