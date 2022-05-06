from OwlToRdf.conversion_owl_to_rdf import remove_restriction

def test_remove_restriction():
    triples = [('a.only(b)', 'a & b', 'a | b')]
    assert remove_restriction(triples) == []

    triples = [('a', 'b', 'c'), ('d', 'e', 'f')]
    assert remove_restriction(triples) == triples

    triples = [('a', 'b', 'c'), ('a.only(b)', 'a & b', 'a | b'), ('d', 'e', 'f')]
    assert remove_restriction(triples) == [('a', 'b', 'c'), ('d', 'e', 'f')]

    triples = [('a', 'b', 'c'), ('a.only(b)', 'a', 'b'), ('d', 'e', 'f')]
    assert remove_restriction(triples) == [('a', 'b', 'c'), ('d', 'e', 'f')]

    triples = [('a', 'b', 'c'), ('a', 'a & b', 'b'), ('d', 'e', 'f')]
    assert remove_restriction(triples) == [('a', 'b', 'c'), ('d', 'e', 'f')]

    triples = [('a', 'b', 'c'), ('a', 'b', 'a | b'), ('d', 'e', 'f')]
    assert remove_restriction(triples) == [('a', 'b', 'c'), ('d', 'e', 'f')]

    triples = [('pizza.American', 'subClassOf', 'pizza.hasTopping.only(pizza.MozzarellaTopping | pizza.PeperoniSausageTopping | pizza.TomatoTopping)')]
    assert remove_restriction(triples) == []


