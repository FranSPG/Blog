#include <sys/shm.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#define ROJO 0
#define VERDE 1
#define JUGADOR 1
#define CANTIDAD 3
#define MANO_DESDE 1
#define MANO_HASTA 5
#define VERIFICAR 1500


typedef struct paneles panel;

struct paneles
{
	int jugador1; // 0 = NADA, 1 = PIEDRA, 2 = PAPEL, 3 = TIJERAS, 4 = LAGARTO, 5 = SPOCK
	int jugador2;
	int estado; // 0 = NO JUGO NADIE, 1 = GANO 1, 2 = GANO 2
};

key_t creo_clave()
{
	// Igual que en cualquier recurso compartido (memoria compartida, semaforos
	// o colas) se obtien una clave a partir de un fichero existente cualquiera
	// y de un entero cualquiera. Todos los procesos que quieran compartir este
	// memoria, deben usar el mismo fichero y el mismo entero.
	key_t clave;
	clave = ftok ("/bin/ls", 30);
	if (clave == (key_t)-1)
	{
		printf("No puedo conseguir clave para memoria compartida\n");
		exit(0);
	}
	return clave;
}

void* creo_memoria(int size, int* r_id_memoria)
{
	void* ptr_memoria;
	int id_memoria;
	id_memoria = shmget (creo_clave(), size, 0777 | IPC_CREAT);

	if (id_memoria == -1)
	{

		printf("No consigo id para memoria compartida\n");
		exit (0);
	}

	ptr_memoria = (void *)shmat (id_memoria, (char *)0, 0);

	if (ptr_memoria == NULL)
	{
		printf("No consigo memoria compartida\n");

		exit (0);
	}
	*r_id_memoria = id_memoria;
	return ptr_memoria;
}

//funcion que crea el semaforo
int creo_semaforo()
{
  key_t clave = creo_clave();
  int id_semaforo = semget(clave, 1, 0600|IPC_CREAT);
  //PRIMER PARAMETRO ES LA CLAVE, EL SEGUNDO CANT SEMAFORO, EL TERCERO 0600 LO UTILIZA CUALQUIERA, IPC ES CONSTANTE (VEA SEMAFORO)
  if(id_semaforo == -1)
  {
      printf("Error: no puedo crear semaforo\n");
      exit(0);
  }
  return id_semaforo;
}

//inicia el semaforo
void inicia_semaforo(int id_semaforo, int valor)
{
	semctl(id_semaforo, 0, SETVAL, valor);
}

//levanta el semaforo
void levanta_semaforo(int id_semaforo)
{
	struct sembuf operacion;
	printf("\nLevanta SEMAFORO \n");
	operacion.sem_num = 0;
	operacion.sem_op = 1; //incrementa el semaforo en 1
	operacion.sem_flg = 0;
	semop(id_semaforo,&operacion,1);
}

//espera semaforo
void espera_semaforo(int id_semaforo)
{
	struct sembuf operacion;
	printf("Espera SEMAFORO \n");
	operacion.sem_num = 0;
	operacion.sem_op = -1; //decrementa el semaforo en 1
	operacion.sem_flg = 0;
	semop(id_semaforo,&operacion,1);

}

int main(int argc, char *argv[])
{
	panel *memoria = NULL;
	int id_memoria;
	int i, aleatorio;
	int id_semaforo;
	int jugada, posicion;
	int jugador = JUGADOR;

	if(argc > 1)
	{
		if(atoi(argv[1]) == 1 || atoi(argv[1]) == 2)
		{
			jugador = atoi(argv[1]);
		}
		else
		{
			printf("\nJugador invalido\n");
			return -1;
		}

	}
	printf("Jugador %d\n", jugador);

	srand(time(NULL)-jugador);//cambia la semilla para random,  usa el time como semilla inicial

	id_semaforo = creo_semaforo();

	inicia_semaforo(id_semaforo, VERDE);

	memoria = (panel*)creo_memoria(sizeof(panel)*CANTIDAD, &id_memoria);

	posicion = -1;
	i = 0;
	while(1)
	{

		espera_semaforo(id_semaforo);

		if(i < CANTIDAD)
		{
			jugada = rand()%(MANO_HASTA-MANO_DESDE+1)+MANO_DESDE;
			printf("\nJugador:\t%d\tJugada:\t%d", jugador, jugada);
			posicion = i;
			if(jugador == 2)
			{
				if(memoria[posicion].jugador2 == 0)
				{
					memoria[posicion].jugador2 = jugada;

				}
			}
			else
			{
				if(memoria[posicion].jugador1 == 0)
				{
					memoria[posicion].jugador1 = jugada;
				}
			}

			if(memoria[posicion].jugador1 != 0 && memoria[posicion].jugador2 != 0)
			{
				if(memoria[posicion].jugador1 == memoria[posicion].jugador2)
				{
					memoria[posicion].jugador1 == 0;
					memoria[posicion].jugador2 == 0;
				}
				else
				{
					switch (memoria[posicion].jugador1)
					{
						case 1:
							if(memoria[posicion].jugador2 == 3 || memoria[posicion].jugador2 == 4)
							{
								memoria[posicion].estado = 1;
							}
							else
							{
								memoria[posicion].estado = 2;
							}
							break;
						case 2:
							if(memoria[posicion].jugador2 == 1 || memoria[posicion].jugador2 == 5)
							{
								memoria[posicion].estado = 1;
							}
							else
							{
								memoria[posicion].estado = 2;
							}
							break;
						case 3:
							if(memoria[posicion].jugador2 == 2 || memoria[posicion].jugador2 == 4)
							{
								memoria[posicion].estado = 1;
							}
							else
							{
								memoria[posicion].estado = 2;
							}
							break;
						case 4:
							if(memoria[posicion].jugador2 == 2 || memoria[posicion].jugador2 == 5)
							{
								memoria[posicion].estado = 1;
							}
							else
							{
								memoria[posicion].estado = 2;
							}
							break;
						case 5:
							if(memoria[posicion].jugador2 == 1 || memoria[posicion].jugador2 == 3)
							{
								memoria[posicion].estado = 1;
							}
							else
							{
								memoria[posicion].estado = 2;
							}
							break;
					}

				}
				printf("\nEl ganador de la mano %d fue %d", posicion, memoria[posicion].estado);				
			}

		}
		else
		{
			printf("\nJUEGO TERMINADO\n");
			return -1;
		}

		i++;
		levanta_semaforo(id_semaforo);
		usleep(VERIFICAR*1000);

	};

return 0;
}
