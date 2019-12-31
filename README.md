# Intuitive Ordinal Notations (IONs)

In ["Measuring the Intelligence of an Idealized Mechanical Knowing Agent"](https://semitrivial.github.io/MeasuringIntelligence2019.pdf),
we presented an intuitive ordinal notation system and
argued that the task of notating computable ordinals is a
task that gets directly at the heart of what it means to be
intelligent. This library contains some
examples of ordinal notations. Currently, the
largest example in the library is ω<sup>ω</sup>.

Think of this library as a meditation on automated code generation.
The ordinal notations in this library are themselves computer
programs which output ordinal notations (except for 0.py, which
outputs nothing). The notation for ω<sup>ω</sup> is a computer program which
could, by its lonesome, be used to programmatically reproduce
computer programs equivalent to all the lesser ordinal notations
in the library.

## Reading Order

We recommend the ordinal notations in this library be read in the following
order. Take time to reflect on each program and understand it before
proceeding to the next.

### Level 1 (0 to ω)

* 0 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv1/0.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv1/compiled/0.py)
* 1 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv1/1.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv1/compiled/1.py)
* 2 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv1/2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv1/compiled/2.py)
* 3 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv1/3.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv1/compiled/3.py)
* ω [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv1/w.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv1/compiled/w.py)

### Level 2 (ω to ω<sup>2</sup>)

* ω [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/w.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/compiled/w.py)
* ω+1 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/w+1.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/compiled/w+1.py)
* ω+2 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/w+2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/compiled/w+2.py)
* ω+3 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/w+3.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/compiled/w+3.py)
* ω·2 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/w*2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/compiled/w*2.py)
* ω·2+1 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/w*2+1.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/compiled/w*2+1.py)
* ω·2+2 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/w*2+2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/compiled/w*2+2.py)
* ω·3 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/w*3.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/compiled/w*3.py)
* ω<sup>2</sup> [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/w^2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv2/compiled/w^2.py)

### Level 3 (ω to ω<sup>3</sup>)

* ω [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv3/w.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv3/compiled/w.py)
* ω<sup>2</sup> [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv3/w^2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv3/compiled/w^2.py)
* ω<sup>2</sup>+ω [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv3/w^2+w.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv3/compiled/w^2+w.py)
* ω<sup>2</sup>+ω·2 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv3/w^2+w*2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv3/compiled/w^2+w*2.py)
* ω<sup>2</sup>·2 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv3/w^2*2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv3/compiled/w^2*2.py)
* ω<sup>2</sup>·3 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv3/w^2*3.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv3/compiled/w^2*3.py)
* ω<sup>3</sup> [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv3/w^3.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv3/compiled/w^3.py)

### Level 4 (ω to ω<sup>4</sup>)

* ω [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/w.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/compiled/w.py)
* ω<sup>2</sup> [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/w^2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/compiled/w^2.py)
* ω<sup>3</sup> [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/w^3.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/compiled/w^3.py)
* ω<sup>3</sup>+ω<sup>2</sup> [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/w^3+w^2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/compiled/w^3+w^2.py)
* ω<sup>3</sup>+ω<sup>2</sup>·2 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/w^3+w^2*2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/compiled/w^3+w^2*2.py)
* ω<sup>3</sup>·2 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/w^3*2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/compiled/w^3*2.py)
* ω<sup>3</sup>·2+ω<sup>2</sup> [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/w^3*2+w^2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/compiled/w^3*2+w^2.py)
* ω<sup>3</sup>·2+ω<sup>2</sup>·2 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/w^3*2+w^2*2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/compiled/w^3*2+w^2*2.py)
* ω<sup>3</sup>·3 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/w^3*3.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/compiled/w^3*3.py)
* ω<sup>4</sup> [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/w^4.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv4/compiled/w^4.py)

### Level 5 (1 to ω<sup>ω</sup>)

* 1 [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv5/1.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv5/compiled/1.py)
* ω [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv5/w.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv5/compiled/w.py)
* ω<sup>2</sup> [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv5/w^2.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv5/compiled/w^2.py)
* ω<sup>3</sup> [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv5/w^3.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv5/compiled/w^3.py)
* ω<sup>4</sup> [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv5/w^4.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv5/compiled/w^4.py)
* ω<sup>ω</sup> [With Commentary](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv5/w^w.py) or [Compiled and Uncommented](https://raw.githubusercontent.com/semitrivial/ions/master/src/Lv5/compiled/w^w.py)