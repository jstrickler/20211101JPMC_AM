
struct person {
    char *fname;
    char *lname;
    int age;
}

p = person;
p.name = "Bob";

printf("Name is %s\n", p.name);