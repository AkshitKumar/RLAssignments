#ifndef __ACTION_H
#define __ACTION_H

#include "header.h"

class action {
  public:
    int num_young;
    int num_breedable;
    int num_old;
    action(int, int, int);
    action(action*);
    bool equals(action*);
};
#endif // __ACTION_H
