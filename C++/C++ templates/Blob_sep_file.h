#include <vector>
#include <memory>
#include <iostream>
template<typename T> class Blob;
template<typename T> std::ostream& operator<<(std::ostream& os,const Blob<T>& sb);
template<typename T>
class Blob{
    public:
    typedef T value_type;
    typedef typename std::vector<T>::size_type size_type; // `typename` here is required. TODO: size_type is a member type of std::vector<T>, due to ambiguity explained in C++ Primer pp. 670, one need to use `typename` before `std::vector<T>::size_type` to show that `std::vector<T>::size_type` is a type member, not a static variable member
    Blob();
    Blob(std::initializer_list<T> il);
    template<typename It> Blob(It b, It e); // A constructor that itself is a template function
    size_type size() const {return data->size();}
    bool empty() const {return data->empty();}
    void push_back(const std::string &t) {data->push_back(t);}
    void pop_back();
    T& front();
    T& back();
    private:
    std::shared_ptr<std::vector<T>> data;
    void check(size_type i, const T& msg) const;
    friend std::ostream& operator<<  <> // This <> here makes operator<< to behave as a template function
    (std::ostream&,const Blob<T>&);
    
};