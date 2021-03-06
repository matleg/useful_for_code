
##  accessibility levels 

from : https://gist.github.com/mrkline/8302959


    public               - All code can access this.
    internal             - Only other code in this assembly (i.e. program or library) can access this.
                           This can be useful if you are making a library and want to
                           make classes or methods inaccessible to the end-user.
    protected            - Only other code in this class and derived classes can access this.
    protected internal   - Only other code in this class and derived classes in this assembly can access this.
    private              - Only other code in this class can access this.



##  virtual 

from SO:

The Virtual Modifier is used to mark that a method\property can be modified
in a derived class by using the override modifier.

Example:

class A
{
    public virtual void Foo()
       //DoStuff For A
}

class B : A
{
    public override void Foo()
    //DoStuff For B

    //now call the base to do the stuff for A and B
    //if required
    base.Foo()
}



##  abstract classes 

from : https://members.loria.fr/ABelaid/Enseignement/FC/Cours7-Classes-abstraites.pdf
       https://zaiste.net/abstract_classes_in_python/
       https://stackoverflow.com/questions/17088346/mimic-python-pure-virtual-functions-like-c-sharp


Le mécanisme des classes abstraites permet de définir des comportements (méthodes) dont l'implémentation
(le code dans la méthode) se fait dans les classes filles.
Ainsi, on a l'assurance que les classes filles respecteront le contrat défini par la classe mère abstraite.
 Ce contrat est une interface de programmation.

Prenons l'exemple suivant : vous avez une classe Humain, à partir de laquelle dérivent la classe Homme
et la classe Femme. En toute logique, Homme et Femme sont instanciables (les objets créés ont une existence en soi),
 mais la classe Humain sera déclarée abstraite car un objet Humain n'existe pas en tant que tel, puisqu'il
 manque l'information sur le sexe. Ici, la classe Humain servira à implémenter des méthodes qui seront utilisées
 à la fois pour Homme et pour Femme.


Because of Python's dynamic nature there are few things being checked during compilation,
and there is no advanced type checking at that stage. For that reason, we could declare an abstract method
 by just raising a NotImplementedError.

class Animal:

    def say_something(self):
        raise NotImplementedError()

Additionaly, a class could follow some naming conventions e.g. prefixing a class name with Base or Abstract.


Speaking about run-times errors. Python is a dynamic language, so, well, that's how it works.
 A common idiom is raising NotImplementedError in __init__ to show that your class is abstract
 (and the same is true for abstract (pure virtual) methods). You can also have a look at abc as
 it does what you want: it prohibits instantiation of abstract classes. But I also strongly
 suggest reading PEP-3119 to understand what Abstract Base Classes are and what they are not.

AFAIK, raising NotImplementedError is enough for pylint to understand that your class/method is abstract.



##   




##   


##   




##   


##   