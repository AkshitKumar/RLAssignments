/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : action.cpp

* Purpose : Herd Management Assignment

* Creation Date : 02-10-2013

* Last Modified : Sun 06 Oct 2013 03:38:08 PM IST

* Created By : npsabari

_._._._._._._._._._._._._._._._._._._._._.*/

#include "action.h"

action::action(int _num_young, int _num_breedable, int _num_old) {
  this->num_young = _num_young;
  this->num_breedable = _num_breedable;
  this->num_old = _num_old;
}

action::action(action* _action) {
  this->num_young = _action->num_young;
  this->num_breedable = _action->num_breedable;
  this->num_old = _action->num_old;
}

bool action::equals(action* other) {
  return (this->num_young == other->num_young && this->num_breedable == other->num_breedable && this->num_old == other->num_old);
}
