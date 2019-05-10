<h2>Περιγραφή:</h2>
Πρόκειται για ένα αυτόνομο ρομπότ που αναγνωρίζει ανθρώπινα πρόσωπα και σε
περίπτωση εισβολής μη αναγνωρίσιμου προσώπου τις ώρες που το σχολείο είναι κλειστό
θα ενημερώνει με email το κατάλληλο πρόσωπο.
Το ρομπότ λειτουργεί σε δύο καταστάσεις:
<ol>
 	<li><strong>Κατάσταση Σχολικού φύλακα, σε ώρες εκτός σχολικού ωραρίου</strong></li>
 	<li><strong>Κατάσταση ψυχαγωγίας (χαιρετισμός - αναγνώριση,μουσική, βόλτες), σε ώρες εντός σχολικού ωραρίου</strong></li>
</ol>
<strong>Στην 1 η κατάσταση</strong> (δηλ. τις ώρες εκτός σχολικού ωραρίου), το ρομπότ θα κινείται στον
χώρο του σχολείου ανιχνεύει για πρόσωπα και στην περίπτωση μη αναγνωρίσιμου
προσώπου ενημερώνει με email τον Διευθυντή του σχολείου

<strong>Στην 2 η κατάσταση</strong> (εντός σχολικού ωραρίου), το ρομπότ μπορεί να βρίσκεται σε διάφορες
καταστάσεις όπως: <strong>ηρεμία</strong>,<strong> κίνηση στο χώρο του σχολείου</strong>, <strong>αναγνώριση και χαιρετισμός</strong>
<strong>ονομαστικά προσώπων που συναντάει</strong>, <strong>παίξιμο μουσικής</strong>. Τα παραπάνω γίνονται <strong>τυχαία</strong>. Κάθε λίγο αλλάζει υποκατάσταση.

<img class="size-medium aligncenter" src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/robotDesc1.png?raw=true" width="531" height="229" />

&nbsp;

<img class="size-medium aligncenter" src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/robotDesc2.png?raw=truehttp://" width="591" height="326" />
<h2>Παρουσίαση δυνατοτήτων:</h2>
<a href="https://www.youtube.com/watch?v=UrVr22XGyjo" rel="nofollow">[youtube https://www.youtube.com/watch?v=UrVr22XGyjo&amp;w=1280&amp;h=753]</a>
<h2>Αποθετήρια &amp; OER CANVAS</h2>
Αποθετήριο στο github: <a href="https://github.com/panos3oesp/sxolikosfylakas" target="_blank" rel="noopener">πατήστε εδώ</a>
Project OER CANVAS: <a href="https://github.com/panos3oesp/sxolikosfylakas/raw/master/OER%20PROJECT.pdf" target="_blank" rel="noopener">πατήστε εδώ</a>

&nbsp;

&nbsp;
<h2><img class="alignnone " src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/makingOf1.jpg?raw=true" width="296" height="444" /> <img class="alignnone " src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/8.jpg?raw=true" width="296" height="444" /> <img class="alignnone " src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/makingOf6.jpg?raw=true" width="296" height="444" /> <img class="alignnone " src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/3.jpg?raw=true" width="296" height="444" /></h2>
<h2><img class="alignnone " src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/4.jpg?raw=true" width="296" height="444" /> <img class="alignnone " src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/5.jpg?raw=true" width="296" height="444" /> <img class="alignnone " src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/6.jpg?raw=true" width="296" height="444" /> <img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/7.jpg?raw=true" width="296" height="444" /></h2>
<h2><a id="user-content-κώδικας---δομή" class="anchor" href="https://github.com/panos3oesp/sxolikosfylakas/blob/master/README.md#%CE%BA%CF%8E%CE%B4%CE%B9%CE%BA%CE%B1%CF%82---%CE%B4%CE%BF%CE%BC%CE%AE"></a>Κώδικας - Δομή</h2>
Ο Κώδικας είναι γραμμένος σε γλώσσα προγραμματισμού <b>python 3.7+</b>. Ως αρχή διαχωρισμού του κώδικα σε στοιχεία, χρησιμοποιείται όπου είναι δυνατόν το πρότυπο <b>MVC</b> (Model - View - Controller). Ως views προς το παρόν θα είναι διαγνωστικά μηνύματα. Σε μελλοντική αναβάθμιση, θα είναι αλλαγές σε συνδεδεμένη οθόνη. Επιπλέον ο φάκελος
Helpers περιέχει βοηθιτικές κλάσεις υπεύθυνες για παράδειγμα για να στέλνει το ρομπότ email, να μιλάει με τη βάση δεδομένων (γενικά ως διεπαφή). Ο Φάκελος res περιέχει αρχεία βοηθητικά, όπως φωτογραφίες, βάση δεδομένων κ.τ.λ.
<ul>
 	<li>Models/ (κλάσεις επικοινωνία με βάση για κάθε οντότητά της)</li>
 	<li>Views/ (κλάσεις μόνο για προβολή διαγνωστικών, αργότερα προβολή εκφράσεων κτλ σε οθόνη)</li>
 	<li>Controller/ (κλάσεις σχετικά με τον έλεγχο των λειτουργιών του ρομπότ)</li>
 	<li>Helpers/ (βοηθητικές κλάσεις που διευκολύνουν την εφαρμογή ως διεπαφή και όχι μόνο)</li>
 	<li>res/ (αρχεία όπως εικόνες, βάση δεδομένων). Ο φάκελος faces έχει τις εικόνες από τα πρόσωπα. Το αρχείο dataset_faces.dat περιέχει τα πρόσωπα αναλυμένα. Το αρχείο robot2.sqlite περιέχει τα στοιχεία των ατόμων που γνωρίζει το σύστημα και τα μονοπάτια των φωτογραφιών.
<ul>
 	<li>images/ (εικόνες)</li>
 	<li>robot.db (βάση δεδομένων)</li>
</ul>
</li>
 	<li>configuration.py (αρχείο ρυθμίσεων)</li>
</ul>
<h2><a id="user-content-διάγραμμα-ροής" class="anchor" href="https://github.com/panos3oesp/sxolikosfylakas/blob/master/README.md#%CE%B4%CE%B9%CE%AC%CE%B3%CF%81%CE%B1%CE%BC%CE%BC%CE%B1-%CF%81%CE%BF%CE%AE%CF%82"></a>Διάγραμμα Ροής</h2>
<a href="https://github.com/panos3oesp/sxolikosfylakas/blob/master/robot.pdf"><img class="alignnone size-medium" src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/diagramma_rois.png?raw=true" width="2000" height="1877" /></a>
<h2><span style="color: #24292e;"><u><b>Διδακτική προσέγγιση:</b></u></span></h2>
<span style="color: #24292e;">Στη συνέχεια, για την πραγματοποίηση του </span><span style="color: #24292e;"><span lang="en-US">project</span></span><span style="color: #24292e;">,δημιουργήθηκαν από κοινού ομάδες εργασίας των μαθητών με κριτήριο την τάξη που φοιτούν και την δυσκολία που μπορεί να παρουσιάζει ο κάθε επί μέρους κώδικας. Ο στόχος ήταν η κάθε ομάδα να αναπτύξει δεξιότητες συναφείς με την γνώση που είχαν ήδη αποκτήσει.</span>

<span style="color: #24292e;">Η διδακτική προσέγγιση που ακολουθήθηκε από τους εκπαιδευτικούς –υπεύθυνους για το συγκεκριμένο </span><span style="color: #24292e;"><span lang="en-US">project</span></span><span style="color: #24292e;">, βασίζεται στις καινούργιες αρχές-τάσεις που αφορούν στη μάθηση, μερικές από αυτές περιγράφονται παρακάτω:</span>
<ul>
 	<li><span style="color: #24292e;">Ενεργός συμμετοχή των μαθητών, ώστε να αξιοποιούν την φυσική τους διάθεση για διερεύνηση νέων πραγμάτων</span></li>
 	<li><span style="color: #24292e;">Κοινωνική αλληλεπίδραση με σκοπό να εξωτερικεύουν τις ιδέες τους μέσα σε μια ομάδα</span></li>
 	<li><span style="color: #24292e;">Δραστηριότητες που έχουν νόημα για τους μαθητές, που καταλαβαίνουν τον λόγο για τον οποίο τις κάνουν και είναι μέσα στην κουλτούρα τους.</span></li>
 	<li><span style="color: #24292e;">Σύνδεση των νέων τεχνολογιών με τις προϋπάρχουσες γνώσεις που ενεργοποιούνται και χρησιμεύουν στην ικανότητα της κατανόησης</span></li>
 	<li><span style="color: #24292e;">Χρήση στρατηγικών μάθησης ώστε οι μαθητές να αναλαμβάνουν περισσότερες ευθύνες</span></li>
 	<li><span style="color: #24292e;">Ανάπτυξη του αναστοχασμού των μαθητών, ώστε να σχεδιάζουν και να παρακολουθούν οι ίδιοι τη μάθηση τους και να διορθώνουν τα λάθη τους</span></li>
 	<li><span style="color: #24292e;">Αναδόμηση της προϋπάρχουσας γνώσης ώστε αυτή να μην αποτελεί εμπόδιο για τα νέα γνωστικά αντικείμενα</span></li>
 	<li><span style="color: #24292e;">Στόχος η κατανόηση και όχι η απομνημόνευση</span></li>
 	<li><span style="color: #24292e;">Διάθεση χρόνου για εξάσκηση των μαθητών που είναι απαραίτητη για την συγκρότηση της γνώσης</span></li>
 	<li><span style="color: #24292e;">Καλλιέργεια κινήτρων για μάθηση που οι μαθητές καθοδηγούμενοι από τον εκπαιδευτικό συμμετέχουν ενεργά σε δραστηριότητες.</span></li>
</ul>
<h2><a id="user-content-υλικά" class="anchor" href="https://github.com/panos3oesp/sxolikosfylakas/blob/master/README.md#%CF%85%CE%BB%CE%B9%CE%BA%CE%AC"></a>Υλικά</h2>
Πρόκειται να χρησιμοποιήσουμε τα παρακάτω υλικά:
<table>
<tbody>
<tr>
<th>α/α</th>
<th>Όνομα</th>
<th>τεμάχια</th>
<th>κόστος</th>
</tr>
<tr>
<td>1</td>
<td><a href="https://grobotronics.com/pir-sensor-module.html" rel="nofollow">Αισθητήρας Ανίχνευσης Κίνησης HC-SR501</a></td>
<td>2</td>
<td>5.60</td>
</tr>
<tr>
<td>2</td>
<td><a href="https://grobotronics.com/infrared-proximity-sensor-sharp-gp2y0a21yk.html" rel="nofollow">Αισθητήρας Απόστασης Υπέρυθρος - Sharp GP2Y0A21YK</a></td>
<td>4</td>
<td>47,60</td>
</tr>
<tr>
<td>3</td>
<td><a href="https://grobotronics.com/power-supply-5v-2.5a-raspberry-pi-official-black.html" rel="nofollow">Τροφοδοτικό 5V 2.5A για Raspberry Pi Μαύρο (Γνήσιο)</a></td>
<td>1</td>
<td>9.90</td>
</tr>
<tr>
<td>4</td>
<td><a href="https://grobotronics.com/micro-sd-16gb-pre-loaded-with-noobs.html" rel="nofollow">Micro SD 16GB - Pre-Loaded with NOOBS</a></td>
<td>1</td>
<td>13.90</td>
</tr>
<tr>
<td>5</td>
<td><a href="https://grobotronics.com/raspberry-pi-heatsink-silver-set-of-3.html" rel="nofollow">Raspberry Pi Heatsink - Black (Set of 2)</a></td>
<td>1</td>
<td>1.20</td>
</tr>
<tr>
<td>6</td>
<td><a href="https://grobotronics.com/raspberry-pi-camera-module-noir-v2-8mp-1080p.html" rel="nofollow">Raspberry Pi Camera Module  (8MP,1080p)</a></td>
<td>1</td>
<td>29.90</td>
</tr>
<tr>
<td>7</td>
<td><a href="https://grobotronics.com/waveshare-rpi-motor-driver-hat.html" rel="nofollow">Waveshare RPi Motor Driver HAT</a></td>
<td>1</td>
<td>34.90</td>
</tr>
<tr>
<td>8</td>
<td><a href="https://grobotronics.com/raspberry-pi-3-model-b-el.html" rel="nofollow">Raspberry Pi 3 - Model B+</a></td>
<td>1</td>
<td>41.90</td>
</tr>
<tr>
<td>9</td>
<td>Μπαταρίες 6V</td>
<td>2</td>
<td>11,20</td>
</tr>
</tbody>
</table>
<b>Το συνολικό κόστος είναι 196,10 Ευρώ.</b>
<h2>Ηλεκτρονικό Κύκλωμα</h2>
<img class="size-medium aligncenter" src="https://github.com/panos3oesp/sxolikosfylakas/raw/master/ilektroniko_kykloma_big.png" width="600" height="744" />

Η κεντρική ιδέα είναι η εξής:
<ul>
 	<li>Το Raspberry, υπεύθυνο για την εκτέλεση του αλγορίθμου σε γλώσσα προγραμματισμού python 3.</li>
 	<li>Οι αισθητήρες απόστασης λαμβάνουν αναλογικό σήμα του οποίου η τάση, volts είναι αντιστρόφως ανάλογη της απόστασης.  Υπάρχουν 4 αισθητήρες, ένας για κάθε πλευρά.</li>
 	<li>Το Anrduino λαμβάνει ρεύμα από το usb port μέσω του Raspberry και μετατρέπει τις αναλογικές τιμές από τους αισθητήρες σε ψηφιακή και τις αποστέλλει στο Raspberry.</li>
 	<li>H Κάμερα λαμβάνει συνεχώς εικόνες τις οποίες επεξεργάζεται το Raspberry χρησιμοποιώντας την face_recognition library της python.</li>
 	<li>To motor hat λαμβάνει 12V από τις μπαταρίες και διοχετεύει 5v στο Rasberry.</li>
 	<li>Το motor hat λαμβάνει εντολές από το Raspberry και δίνει έως 12V στα moter.  Ακολουθεί τη φιλοσοφία ενός Tank.
<ul>
 	<li>Αν δοθεί ρεύμα και στα 2 μοτέρ το ρομποτ κινείται μπροστά.</li>
 	<li>Αν δοθεί ρεύμα στο δεξί, στρίβει αριστερά. (με ανάποδη τάση στο άλλο μοτέρ στρίβει γρηγορότερα)</li>
 	<li>Αν δοθεί ρεύμα στο αριστερό, στρίβει δεξιά. (με ανάποδη τάση στο άλλο μοτέρ στρίβει γρηγορότερα)</li>
 	<li>Αν δοθεί ανάποδη τάση και στα δύο, οπισθοχωρεί.</li>
</ul>
</li>
</ul>
<img class="size-medium aligncenter" src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/explain_electronics.jpg?raw=true" width="1024" height="683" />
<h2><a id="user-content-σχέδιο-τομή" class="anchor" href="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/designB2.png?raw=true"></a>Σχέδιο Τομή</h2>
<a href="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/designB2.png?raw=true" target="_blank" rel="noopener noreferrer"><img class="aligncenter" src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/designB2.png?raw=true" /></a>
<h2><a id="user-content-κάτοψη" class="anchor" href="https://github.com/panos3oesp/sxolikosfylakas/blob/master/README.md#%CE%BA%CE%AC%CF%84%CE%BF%CF%88%CE%B7"></a>Κάτοψη</h2>
<a href="https://github.com/panos3oesp/sxolikosfylakas/blob/master/designA.png" target="_blank" rel="noopener noreferrer"><img class="aligncenter" src="https://github.com/panos3oesp/sxolikosfylakas/raw/master/designA.png" /></a>

&nbsp;
<h2>Καταμερισμός Εργασιών</h2>
<table>
<tbody>
<tr>
<th>α/α</th>
<th>Υποέργο</th>
<th>Υπεύθυνοι</th>
</tr>
<tr>
<td>1</td>
<td>Ηλεκτρονικά</td>
<td>Παναγιώτης (ΓΠ)
Γιώργος (ΒΠ)</td>
</tr>
<tr>
<td>2</td>
<td>Κίνηση Ρομπότ - Κώδικας</td>
<td>Θεοδωρής (ΓΠ)
Βαλάντης (ΓΠ)</td>
</tr>
<tr>
<td>3</td>
<td>Αναγνώριση Προσώπου</td>
<td>Μίλτος (ΔΠ)
Μαρία Τ.(ΒΠ)
Ελβίρα(ΔΠ)
Μιχάλης (ΔΠ)</td>
</tr>
<tr>
<td>4</td>
<td>Ήχος</td>
<td>Νίκος (ΓΠ)
Ταξιάρχης(ΓΠ)</td>
</tr>
<tr>
<td>5</td>
<td>Αποστολή email</td>
<td>Μαρία Β. (ΔΠ)
Μαρία M.(ΒΠ)
Ματινα Μ.(ΒΠ)</td>
</tr>
<tr>
<td>6</td>
<td>Βίντεο</td>
<td>Αργύρης (ΒΠ)
Στέφανος(ΒΠ)</td>
</tr>
<tr>
<td>7</td>
<td>Μηχανικό Μέρος</td>
<td>Μιχάλης (ΓΠ)
Παναγιώτης (ΓΠ)
Γιώργος (ΒΠ)</td>
</tr>
<tr>
<td>8</td>
<td>Επίβλεψη</td>
<td>Μίλτος (ΔΠ)</td>
</tr>
</tbody>
</table>
<h2>Υλικό από τις φάσεις υλοποίησης</h2>
<h3>Φάση 1 - Σχεδιασμός - Εργασία σε ομάδες</h3>
<a href="https://www.youtube.com/watch?v=Pg-1URzjuto" rel="nofollow">[youtube https://www.youtube.com/watch?v=Pg-1URzjuto&amp;w=1280&amp;h=753]</a>

<b>εικόνες:</b>
<img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/sxed1.jpg?raw=true" width="200" /> <img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/sxed2.jpg?raw=true" width="200" /> <img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/sxed3.jpg?raw=true" width="200" />
<h3></h3>
<h3>Φάση 2 - Σασί</h3>
<b>βίντεο:</b> <a href="http://doricsoft.com/robot/fasi1.mp4" target="_blank" rel="noopener">εδώ</a>
<b>εικόνες:</b>
<img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/skeletos1.jpg?raw=true" width="200" /> <img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/skeletos2.jpg?raw=true" width="200" /> <img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/skeletos3.jpg?raw=true" width="200" /> <img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/skeletos4.jpg?raw=true" width="200" />
<h3>Φάση 3 - Raspberry</h3>
<b>βίντεο:</b> <a href="http://doricsoft.com/robot/fasi2.mp4" target="_blank" rel="noopener">εδώ</a>
<b>εικόνες:</b>
<img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/ras1.jpg?raw=true" width="200" /> <img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/ras2.jpg?raw=true" width="200" /> <img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/ras3.jpg?raw=true" width="200" /> <img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/ras4.jpg?raw=true" width="200" />
<h3>Φάση 4 - Arduino</h3>
<b>βίντεο:</b> <a href="https://youtu.be/w9END-3aBro" rel="nofollow">[youtube https://youtu.be/w9END-3aBro&amp;w=1280&amp;h=753]</a>
<b>εικόνες:</b>
<img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/arduinoRasp1.jpg?raw=true" width="200" /> <img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/arduinoRasp2.jpg?raw=true" width="200" />
<h3>Φάση 5 - Moter</h3>
<b>βίντεο:</b>
Δοκιμές χωρίς ελεγκτές:
<a href="https://www.youtube.com/watch?v=PikkqNtC3kI" rel="nofollow">[youtube https://www.youtube.com/watch?v=PikkqNtC3kI&amp;w=1280&amp;h=753]</a>
Πρώτες Δοκιμές με motor controller:
<a href="https://www.youtube.com/watch?v=L-_xVFDmJX4" rel="nofollow">[youtube https://www.youtube.com/watch?v=L-_xVFDmJX4&amp;w=1280&amp;h=753]</a>
<a href="https://www.youtube.com/watch?v=9V1Vu6hdX1A" rel="nofollow">[youtube https://www.youtube.com/watch?v=9V1Vu6hdX1A&amp;w=1280&amp;h=753]</a>
<a href="https://www.youtube.com/watch?v=dsQnqRRhkoQ" rel="nofollow">[youtube https://www.youtube.com/watch?v=dsQnqRRhkoQ&amp;w=1280&amp;h=753]</a>

<b>εικόνες:</b>
<img class="" src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/skeletos_moter.jpg?raw=true" width="200" height="150" />
<h3>Φάση 6 - Αναγνώριση</h3>
<b>βίντεο:</b> <a href="https://youtu.be/9Yb0n_LDOAg" rel="nofollow">[youtube https://youtu.be/9Yb0n_LDOAg&amp;w=1280&amp;h=753]</a>
<h3>Φάση 7 Περίβλημα</h3>
<img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/makingOf2.jpg?raw=true" width="200" /> <img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/makingOf3.jpg?raw=true" width="200" /> <img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/makingOf4.jpg?raw=true" width="200" /> <img src="https://github.com/panos3oesp/sxolikosfylakas/blob/master/images/makingOf5.jpg?raw=true" width="200" />
<h2>Εγκατάσταση Λογισμικού</h2>
Για να εγκαταστήσετε το πρόγραμμα
Εγκαταστήστε python 3.5+
Κάντε Compile τη dlib
ανοίξτε από το res το db αρχείο και βάλτε τα δικά σας στοιχεία για τα άτομα και τα σχετικά μονοπάτια των φωτογραφιών
τρέξτε το python main.py
αν δεν έχετε όλες τις απαιτούμενες βιβλιοθήκες η python θα επιστρέψει σχετικό μήνυμα, τρέξτε το pip install όνομα_αυτης_που_λείπει
<h2>Ενέργειες για το μέλλον</h2>
Πρέπει να κατασκευαστεί ένα περίβλημα για να γίνει αισθητικά ωραιότερο το Ρομπότ.
<h2>Άδεια Χρήσης</h2>
Ο κώδικας διανέμεται με άδεια χρήσης ανοιχτού κώδικα MIT License.
Το εκπαιδευτικό υλικό και η τεκμηρίωση να διανέμεται με άδεια χρήσης <strong>CC-BY</strong>.
