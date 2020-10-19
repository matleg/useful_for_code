
##  static keyword 


from https://callicode.fr/blog/post/variables_statiques_python.html:

```C
void compteur(void){
    static int c = 0;
    c = c + 1;
    printf("Appel n : %d\n",c);
}

void main(void) {
    int i;
    for(i=0;i<3;i++){
    compteur();
    }
}

>Appel n : 1
>Appel n : 2
>Appel n : 3


The static variable c is local to the function compteur but it keeps its value between 2 calls
(thanks to static keyword).
```


python:
```python
def compteur():
    if not hasattr(compteur, 'c'):
        compteur.c = 0
    compteur.c = compteur.c + 1
    print("Appel numéro : ", c)

for i in range(3):
    compteur()
```

##  include 

```C
#include <stdio.h>  --> libraries
#include "game.h"  --> local file

headers like stdio.h, stdlib.h, ... contain prototypes of standard functions (printf...)

<string.h> : strlen, strcmp, strcpy, ...

#ifndef used in .h to avoid infinite inclusions

```



##  array 

fixed size! never : int array[var], always int array[5]

array[1]  <->  *(array+1)  : array is an adress, array[1] is a value 



##  struct example 

```
#include <stdio.h>

typedef struct Personne;

struct Personne
{
    char name[100];
    char surname[100];
    int age;
};

int main(int argc, char const *argv[])
{
    struct Personne pers;
    pers.name[0] = 't';
    pers.name[1] = 'o';
    pers.name[2] = 't';
    pers.name[3] = 'o';
    pers.name[4] = '\0';
    printf("%s", pers.name);

    return 0;
}
```



##  strings 



```C
#include <string.h>

int main(int argc, char const *argv[])
{
    char str[] = {'a', 'b', 'c', '\0'};
    char str2[] = "abcd";  // 2 ways to define strings
    int len ;
    len = strlen(str);

    int comp;
    comp = strcmp(str, str2);
    printf("%s, %s, %d, %d\n", str, str2, len, comp); // abc, abcd, 3, -1

    strncat(str, str2, 2);
    printf("%s \n", str); // abcab

    char s2[] = "blablahblah";
    strcpy(str2, s2);
    printf("%s \n", str2); // blablahblah

    return 0;
}
```

##   


##   






