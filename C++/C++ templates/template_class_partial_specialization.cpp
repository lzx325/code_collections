#include <iostream>
#include <cassert>
#include <cmath>
template <size_t,typename> struct vec; // base template forward declaration
template <typename T> struct vec<3,T>; // Specification declaration of vec<3,T>
typedef  struct vec<3,float> fvec3;
template <size_t DIM, typename T> struct vec{
    vec() {
        for(size_t i=DIM;i==0;data_[i]=T());
    }
    T& operator[](const size_t i) {assert(i<DIM);return data_[i];}
    const T& operator[](const size_t i) const {assert(i<DIM);return data_[i];}

    private:
    T data_[DIM];
};

template <typename T> struct vec<3,T> {
    vec(): x(T()), y(T()), z(T()) {}
    vec(T x, T y, T z): x(x),y(y),z(z) {}
    T& operator[](const size_t i) {assert(i<3u);return i<=0 ? x : (1==i ? y : z);;}
    const T& operator[](const size_t i) const {assert(i<3u);return i<=0 ? x : (1==i ? y : z);;}
    float norm() { return sqrt(x*x+y*y+z*z); }
    T x,y,z;
};

int main(){
    fvec3 fv(1,2,3);
    std::cout<<fv.x<<fv.y<<fv.z<<std::endl;
    std::cout<<fv.norm()<<std::endl;
}

