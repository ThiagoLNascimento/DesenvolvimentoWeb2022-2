from homepage.models import Carousel, CardFront, Banner

carousel1 = Carousel(img="images/carrousel-1.jpg")
carousel2 = Carousel(img="images/carrousel-2.jpg")
carousel3 = Carousel(img="images/carrousel-3.jpg")
carousel4 = Carousel(img="images/carrousel-4.jpg")
carousel5 = Carousel(img="images/carrousel-5.jpg")
carousel6 = Carousel(img="images/carrousel-6.jpg")

carousel1.save()
carousel2.save()
carousel3.save()
carousel4.save()
carousel5.save()
carousel6.save()

banner1 = Banner(url="/piratininga-1.html/", img="images/Piratininga.png")
banner2 = Banner(url="/piratininga-1.html/", img="images/Piratininga.png")
banner3 = Banner(url="/piratininga-1.html/", img="images/Piratininga.png")

banner1.save()
banner2.save()
banner3.save()

cardFront1 = CardFront(title="Luíz Imóveis Itaipu",
                       text="Rua Jefferson Rocha, 165 <br>- Rotatória da Av. Central <br>Itaipu <br>Niterói/RJ <br>(21) 3741-8920",
                       img="images/logo.png",
                       alt="Luis Imóveis",
                       creci="CRECI: 7888J")
cardFront2 = CardFront(title="Luíz Imóveis Piratininga",
                       text="Estrada Francisco da Cruz Nunes, 580 <br>- Barravento<br>Piratininga <br>Niterói/RJ <br>(21) 99974-3384 <br>(21) 2608-0489",
                       img="images/logo.png",
                       alt="Luis Imóveis",
                       creci="CRECI: 7888J")

cardFront1.save()
cardFront2.save()