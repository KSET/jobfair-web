blogApp.controller('LogoModalController', function($scope, logo, close) {
  $scope.logo = logo;
  
   $scope.close = function() {
      close();
      }
  
});

blogApp.controller('BlogCtrl',
  function ($scope, ModalService) {
    
    $scope.logos = [{name:'Acceleratio', src:'img/logos/Acceleratio.png', description: 'Acceleratio je mlado i perspektivno poduzeće iz Zagreba, koja se bavi razvojem i prodajom softverskih alata namijenjenih IT stručnjacima. Naši proizvodi bazirani su na Microsoft SharePoint, Office 365 i Windows, odnosno Citrix server tehnologijama. Preko 2000 organizacija i poduzeća iz cijeloga svijeta prepoznalo je naš talent i trud, a za neke od njih ste sigurno i čuli: Microsoft, Intel, Cisco, Vodafone, Bayer, Olympus, Volkswagen, Coca Cola te mnogi drugi. Zasad se naš tim sastoji od gotovo 30 mladih nada kojima se kontinuirano trudimo omogućiti najbolje uvjete za rad, no uvijek smo u lovu na nove talente. Ukoliko smatraš da si ti jedan od njih ili te samo zanima više o nama potraži nas na www.acceleratio.net i saznaj više!',
                    link: 'https://acceleratio.net/'},
                    {name:'ApisIT', src:'img/logos/ApisIT.png', description: 'APIS IT d.o.o. pruža strateške, stručne i provedbene usluge javnom sektoru Republike Hrvatske u planiranju, razvoju, podršci i održavanju poslovno-informacijskih sustava po principima umrežene korisnički usmjerene uprave. Tijekom niza godina stručnjaci APIS IT-a razvili su vrlo sadržajne i kompleksne informatičke sustave za podršku Poreznoj i Carinskoj upravi te upravi Grada Zagreba koji su i danas u uspješnoj produkciji. Po broju korisnika i online transakcija to su najveći informatički sustavi u našoj zemlji iz čega proizlazi jasna pozicija APIS IT-a u smislu znanja, kvalitete i odgovornosti. Novim projektima u kojima implementiramo najnovija ICT rješenja i arhitekture omogućujemo interoperabilnost i interkonektivnost cjelokupne javne uprave na državnoj i europskoj razini.',
                    link: 'http://www.apis-it.hr/apisit/ws.nsf/public/index?OpenForm'},
                    {name:'AssecoSEE', src:'img/logos/AssecoSEE.png', description: 'Asseco South Eastern Europe (Asseco SEE, ASEE) group is one of the largest IT companies in the area of production and implementation of its own software solutions and services in the region of South Eastern Europe and Turkey. The Company provides ICT solutions for various industry verticals including the financial sector, payment sector, public administration and telecoms. Since October 2009, the shares of Asseco South Eastern Europe (Asseco SEE) have been listed on the Warsaw stock exchange. Asseco SEE group employs over 1,400 people in 13 countries. More than 10 banks out of the 15 largest banks in southeastern Europe are already clients of Asseco SEE. If you want to be a part of our successful team feel free to send us your CV at Human.Resources@asseco-see.hr.',
                    link: 'https://asseco.com/see/'},
                    {name:'Cetitec', src:'img/logos/Cetitec.png', description: "CETITEC is one of the leading Gateway-Software producers for the German automotive industry. Our software solutions enable the connectivity of diverse automotive bus-systems such as CAN, MOST, FlexRay and Ethernet and are in use by major automotive manufacturers such as Daimler, BMW, Porsche, and automotive suppliers such as Bosch, Panasonic and Continental. In addition to our connectivity solutions we also produce PC-tools for laboratory simulation and pre-series testing for configuration, control and test-solutions.",
                    link: 'http://www.cetitec.com/'},
                    {name:'Deloitte', src:'img/logos/Deloitte.png', description: 'Deloitte je u Hrvatskoj prisutan već više od 18 godina te je u tom razdoblju ostvario istaknutu poziciju pružajući usluge visoke kvalitete. S više od 170 stručnjaka, Deloitte pruža usluge uspješnim multinacionalnim poslovnim subjektima, nekim od najvećih nacionalnih poslovnih subjekata te brojnim brzorastućim malim i srednje velikim poduzetnicima regije. Naši međunarodni timovi pružaju profesionalne usluge u četirima glavnim područjima – reviziji, porezima, poslovnom i financijskom savjetovanju, koje se odlikuju visokom kvalitetom, integriranošću i kontinuitetom.',
                    link: 'http://www2.deloitte.com/hr/hr.html'},
                    {name:'FINA', src:'img/logos/FINA.png', description: 'Financijska agencija (Fina) vodeća je hrvatska tvrtka na području financijskog posredovanja. Nacionalna pokrivenost, informatički sustav prokušan na najzahtjevnijim poslovima od nacionalne važnosti te visoka profesionalna razina stručnih timova omogućuju pripremu i provedbu različitih projekata, od jednostavnih financijskih transakcija do najsofisticiranijih poslova u elektroničkom poslovanju.',
                    link: 'http://www.fina.hr/Default.aspx'},
                    
                    {name:'HRCloud', src:'img/logos/HRCloud.png', description: "Tvrtka HR Cloud (Human Resources Cloud) je prije dvije godine osnovana u Splitu kao podružnica američke tvrtke Neogov iz Los Angelesa. Na matičnom američkom tržištu Neogov uspješno posluje već 15 godina sa  preko 1200 enterprise kijenata.  Poslovanje tvrtke je od samog početka temeljeno na SaaS modelu. U HR Cloudu u Hrvatskoj nudimo priliku za rad na modernim produktima za svjetsko tržište u Human Resources domeni. Sudjelovanje na projektima omogućava suradnju s vrhunskim stručnjacima, mogućnost putovanja i usavršavanja u SAD-u. U Splitu, već sada, naše proizvode stvara preko 20 entuzijastičnih, iskusnih i nabrijanih programera, testera, dizajnera i voditelja projekata.",
                    link: 'http://hrcloud.com/'},
                    {name:'Inetndanet', src:'img/logos/Inetndanet.png', description: 'INTENDA NET je brzorastuća IT tvrtka iz Zagreba koja se bavi razvojem vlastitih softverskih rješenja. Dio smo Recro-net grupacije, uspješno poslujemo te plasiramo naše proizvode i rješenja na međunarodnom tržištu. Potencijalnim zaposlenicima možemo ponuditi odličnu radnu atmosferu, izazovan posao, rad u dinamičnom okruženju sa internacionalnim korisnicima, priliku za osobni i profesionalni razvoj. Više informacija o tvrtci INTENDA NET saznajte na http://www.intendanet.hr.',
                    link: 'http://www.intendanet.hr/'},
                    {name:'Infinum', src:'img/logos/Infinum.png', description: 'Infinum ima urede u Hrvatskoj, Sloveniji i Americi, specijaliziran je za razvoj i dizajn mobilnih i web aplikacija. Uspješno posluje već 10 godina, a u posljednje 4 godine narasli su na 65 zaposlenika, kompletno bez vanjskih investicija. Mnoštvom odličnih projekata probili su se van granica Hrvatske i danas im oko 80% prihoda dolazi od izvoza. Na prošlogodišnjoj Deloitteovoj rang-listi nalaze se među 10 najbrže rastućih IT poduzeća u srednjoj Europi.',
                    link: 'https://www.infinum.co/'},
                    {name:'Infobip', src:'img/logos/Infobip.png', description: 'Internacionalna smo IT kompanija, usmjerena na razvoj in-house proizvoda u svijetu mobilnih tehnologija. Na taj način uspjeli smo u manje od 10 godina izgraditi jednu od najvećih messaging platformi s više od 150.000 klijenata iz cijelog svijeta. Ustvari, postoji znatna vjerojatnost da si i sam/a primio/la poruku putem naše platforme, s obzirom da naše tehnologije dosežu trećinu svjetske populacije! Kako bismo uvijek išli ukorak s tržištem, u 34 ureda diljem svijeta zapošljavamo više od 600 znatiželjnih, strastvenih Infobipovaca, što nas čini trenutno najvećom hrvatskom IT kompanijom.',
                    link: 'http://www.infobip.com/'},
                     {name:'IN2', src:'img/logos/IN2.png', description: 'IN2 je osnovan 1992. godine u Zagrebu, a danas je s 12 vlasnički povezanih tvrtki vodeća softverska grupacija u SEE regiji. IN2 grupa je IT rješenjima prisutna u javnom sektoru i upravi, zdravstvu, financijskom sektoru i osiguranju, telekomunikacijama, maloprodaji i veleprodaji, industriji, komunalnim poduzećima i energetici. Svoj uspjeh IN2 prvenstveno temelji na stručnom, iskusnom i ponajprije motiviranom zaposleniku. Vlastiti edukacijski centar za pripravnike, složeni projekti i kontinuirano ulaganje u znanje neka su od obilježja prepoznatljive korporativne kulture koja je temelj stabilnog razvoja kompanije. Danas IN2 grupa zapošljava preko 500 zaposlenika i planira daljnji rast.',
                    link: 'http://www.in2.hr/'},
                    {name:'i-Ways', src:'img/logos/i-Ways.png', description: 'Povijest i-Waysa počinje u Berlinu 1999. Od tada poduzeće i-Ways je naraslo do vodeće pozicije među pružateljima eCommerce riješenja. Razvili smo se internacionalni tim profesionalaca sa referncama u eCommercu, tehnologiji, razvoju softwaera i online marketinga. Trenutno poslujemo iz 4 ureda Njemačka, Atlanta, Hrvatska i Velika Britanija. i-Ways je sinonim za inovatino, integrirano i međunarodno. To je pristup koji smo izabrali pri pružanju najboljih mogućih usluga i tehnologija našim klijentima i partnerima. Osnovana kao tvrtka koja pruža inovativne usluge, uspješno implementiramo eCommerce i tehnološka riješenja za naše klijente te smo uključni u međunarodnu i multi-channel prodaju. Iskutsvo u industriji, znanje i vještine našeg osoblja kao i kontinuirani prijenos najnovije tehnologije našim partnerima i klijentima je ono što nas održava na vodećoj poziciji na tržištu.',
                    link: 'http://www.i-ways.hr/'},
                    {name:'Jungheinrich', src:'img/logos/Jungheinrich.png', description: 'Jungheinrich Systemloesungen develops and provides innovative solutions for warehouse management and warehouse automation. As a company of the internationally active Jungheinrich group with 12,000 employees we ensure that every day millions of goods are transported from logistics centers to the customers as fast as possible. So far, we have successfully completed projects for more than 100,000 customers from all over the world. From optimising existing systems to planning completely new systems to the implementation of the software and successful handover we put in every effort to meet the  customer\'s requirements.',
                    link: 'http://www.jungheinrich.com/'},
                    {name:'Microsoft', src:'img/logos/Microsoft.png', description: "Software engineers at Microsoft are passionate about building technologies that make the world a better place. At Microsoft, you will collaborate with a team of programming experts to solve problems and build some of the world’s most advanced services and devices. Your efforts on the design, development, and testing of next-generation applications will have an impact on millions of people. You are the link between abstract concepts and delivered solutions. Understanding the consumer, solving problems, and building applications that will impact millions of people.",
                    link: 'https://www.microsoft.com/hr-hr/default.aspx'},
                    {name:'mStart', src:'img/logos/mStart.png', description: 'mStart d.o.o., članica Agrokor koncerna, čija uloga je pružanja vrhunskih usluga u području IT-a svim članicama Agrokor koncerna. Zapošljavamo preko 150 visoko specijaliziranih stručnjaka što  mStart d.o.o. svrstava među vodeće kompanije u području IT usluga u Hrvatskoj. Kroz ključna partnerstva i suradnju sa svjetskim liderima u području poslovnih aplikacija i IT infrastrukture naši zaposlenici imaju prilike raditi na  najrecentnijim i najinovativnijim svjetskim tehnologijama kako bi mogli odgovoriti na najzahtjevnije izazove različitih industrija što nas ujedno i specijalizira za pružanje usluga dodane vrijednosti na tržištu regije.',
                    link: 'http://www.agrokor.hr/hr/kompanije/mstart-d-o-o/'},
                    {name:'Nanobit', src:'img/logos/Nanobit.png', description: 'Osnovana 2008., Nanobit je tvrtka specijalizirana za razvoj zaraznih igara visoke kvalitete i najveći je game development studio u Hrvatskoj, s fokusom na casual gaming. Projekte razvijaju isključivo prema vlastitim idejama i plasiraju na međunarodno tržište (te se tako od kreativnosti osnivača i želje za stvaranjem firme u kakvoj bi i sami htjeli raditi razvio Nanobit u današnjem obliku). Radeći u skladu s motom “Crafting bits of fun”, zahvaljujući motivaciji i vještinama sad već skoro 60-članog tima, iza njih su deseci popularnih igara i aplikacija, kao i plasman među top 15 tehnoloških tvrtki s najbržim rastom u Srednjoj Europi te nagrada za EY Poduzetnika godine. Uz uspjeh projekata, na prvom mjestu im je zadovoljstvo zaposlenika i ugodna radna atmosfera, što je sigurno doprinijelo dobivanju priznanja za jednog od Top 3 Najbolja poslodavca u Hrvatskoj 2014., prema istraživanju portala MojPosao',
                    link: 'http://www.nanobit.co/'},
                    {name:'StudentID', src:'img/logos/StudentID.png', description: 'STUDENT ID je program za studente na završnim godinama fakulteta, koji Vam omogućuje da bolje upoznate svoj potencijal, talente, interese, vrijednosti i vještine kao temelj za kvalitetno biranje karijere. Ukratko, što Vam je važno da se osjećate ostvareno i zadovoljno u poslu i van posla. Kroz cijeli program usmjeravamo se na autentičnost studenata kao kandidata za posao te ih potičemo da na se na temelju toga izdvajaju u moru ostalih tražitelja poslova.Ako ste autentični, nemate konkurenciju!',
                    link: ''},
                    {name:'Styria', src:'img/logos/Styria.png', description: 'Styria INTERNATIONAL unutar odjela digitalnog razvoja okuplja najbolje hrvatske web developere, frontend developere i mobile developere s puno iskustva u radu na portalima i aplikacijama za portale. Rad s najmodernijim web i mobile tehnologijama omogućuje nam da uvijek budemo korak ispred tržišta i pratimo najnovije trendove. Odjel digitalnog razvoja povezan je s kompanijama koje pripadaju Styriji Media Group AG iz Austrije specijaliziran za razvoj i održavanje novih portala, mobilnih verzija tih portala i mobilnih aplikacija te intenzivno radi i na internacionalnim projektima.',
                    link: 'http://www.styria.com/en/home'},
                    {name:'Talentarium', src:'img/logos/Talentarium.png', description: 'Što nakon fakulteta? I tebi se vrti po glavi odlazak u inozemstvo? Nisi siguran je li bolja opcija odlazak ili ostanak u Hrvatskoj? Posao tijekom faksa ili dobre ocjene? Hackatoni ili dobra ljetna praksa? Velike ili male firme? Gdje ćeš više naučiti? Koje se tehnologije traže? Sve odgovore na vječna pitanja, ali i ono najvažnije - što je za TVOJ razvoj karijere najvažnije - pronađi na našem štandu, kod svojeg Talentarium konzultanta.',
                    link: 'http://www.talentarium.hr/'},
                    {name:'Talentor', src:'img/logos/Talentor.png', description: 'Talentor Hrvatska dio je međunarodne Talentor grupe specijalizirane za usluge posredovanja pri zapošljavanju, headhuntinga i HR savjetovanja. Naša snaga su preko 110 konzultanata u više od 14 zemalja u Europi. Pružamo niz usluga iz područja upravljanja ljudskim resursima: predselekcija i selekcija, psihologijsko testiranje, headhunting, outplacement program, centar za procjenu, istraživanje radne klime, eRecruiter (software za upravljanje kandidatima) te HR savjetovanje.',
                    link: 'http://talentor.com/'},
                    {name:'Trikoder', src:'img/logos/Trikoder.png', description: 'U suradnji s našim klijentima oživljavamo njihovu poslovnu viziju zahvaljujući napredcima u tehnologiji. Kao tim stručnjaka za različita područja razvoja internet sustava, služimo se širokim spektrom alata i vještina potrebnih za izradu visoko kvalitetnih proizvoda koji se koriste u nizu online poslovnih okruženja, od izdavaštva do prodaje i oglasnika.',
                    link: 'http://www.trikoder.net/'},
                    {name:'ZABA', src:'img/logos/ZABA.png', description: 'Zagrebačka banka, članica Grupe UniCredit, već je godinama vodeća banka u Hrvatskoj; po kvaliteti proizvoda i usluga, tehnološkoj inovativnosti, mreži samouslužnih uređaja te uspješnim poslovnim rezultatima. Zaposlenicima Banke, kojih ima otprilike 4250, pruža se lepeza mogućnosti za ostvarenje osobnog i profesionalnog napredovanja, bio to razvoj unutar Zagrebačke banke ili pak međunarodna karijera u različitim zemljama u kojima Grupa UniCredit djeluje. Pošaljite nam svoj CV na posao@unicreditgroup.zaba.hr i postanite dio našeg velikog, međunarodnog tima!',
                    link: 'http://www.zaba.hr/home/wps/wcm/connect/zaba_hr/zabautils/naslovnica/'}];
    
    
  $scope.showFullLogo = function(logo) {
   //$window.alert(cv);
    ModalService.showModal({
      templateUrl: "templates/logo-modal.html",
      controller: "LogoModalController",
      inputs: {
        logo: logo
      }
       })
   
  }
  
  $scope.timetable = [{name:'Prvi dan', times: [{name: 'Irish Recruiter', time: '09-10', link:''},
                                        {name: 'Trikoder', time: '10-11', link:''},
                                        {name: 'Acceleratio', time: '11-12', link:''},
                                        {name: 'Apis IT', time: '12-13', link:''},
                                        {name: 'FINA', time: '13-14', link:''},
                                        {name: 'Deloitte', time: '14-15', link:''},
                                        {name: 'NANOBIT', time: '15-16', link:''}
                                        
                                        ]},
                      {name:'Drugi dan', times: [{name: 'CETITEC', time: '09-10', link:''},
                                        {name: 'HR Cloud', time: '10-11', link:''},
                                        {name: 'Pet Minuta', time: '11-12', link:''},
                                        {name: 'Styria', time: '12-13', link:''},
                                        {name: 'Microsoft', time: '13-14', link:''},
                                        {name: 'Edukator ID', time: '14-15', link:''},
                                        {name: 'i-Ways', time: '15-16', link:''},
                                        {name: 'Zagrebačka banka', time: '16-17', link:''},
                                        {name: 'Infinum', time: '17-18', link:''},
                                        {name: 'IN2 grupa', time: '18-19', link:''}
                                        
                                        ]}]
  
  });