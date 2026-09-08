"""
training/train_data.py
Real data se generated — 1190 train + 210 val
"""

TRAIN_DATA = [
    ("Invoice to be sent at Machhali Shahar Parao, Naiganj, Tarapur, Jaunpur, Uttar Pradesh 222143.",
     {"entities": [(22, 92, 'ADDRESS')]}),

    ("Email dx4seo5lh2uyvs8dg@gmail.com not verified.",
     {"entities": [(6, 33, 'EMAIL')]}),

    ("Shruti Desai at Metro pillar no, WZ 246 B, 1st Floor, 659 - 660, Main Najafgarh Road, email yuby43gnsggj@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 84, 'ADDRESS'), (92, 114, 'EMAIL')]}),

    ("Card 6083640306794396 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Billing address: W5JR+QCG, Raj Kamal Rd, Near Chhaya Chauraha, Satyapremi Nagar, Barabanki.",
     {"entities": [(17, 90, 'ADDRESS')]}),

    ("Rahul Sharma card 5111620801549173 blocked.",
     {"entities": [(0, 12, 'PERSON'), (18, 34, 'CREDIT_CARD')]}),

    ("Branch office at 328, Azamgarh - Varanasi Marg, Civil Lines, Azamgarh, Kol Baj Bahadur.",
     {"entities": [(17, 86, 'ADDRESS')]}),

    ("Billing address: B-211, Block B, Devli, Sangam Vihar, New Delhi, Delhi 110080.",
     {"entities": [(17, 77, 'ADDRESS')]}),

    ("Please ship to Sadabad Gate, Vibhav Nagar Colony, Nayee Nagla, Hathras.",
     {"entities": [(15, 70, 'ADDRESS')]}),

    ("Office is at nanak pyau AB block, Gopal Nagar Extension, Najafgarh, Delhi, 110043.",
     {"entities": [(13, 81, 'ADDRESS')]}),

    ("Bill sent to ukyx2hq0v74am4y4@gmail.com for card 5508139396484338.",
     {"entities": [(13, 39, 'EMAIL'), (49, 65, 'CREDIT_CARD')]}),

    ("Account linked to oygbn75cf76emavwc2hj@gmail.com.",
     {"entities": [(18, 48, 'EMAIL')]}),

    ("Bill sent to nr4mafyjpm2s7an@gmail.com for card 4805342590794802.",
     {"entities": [(13, 38, 'EMAIL'), (48, 64, 'CREDIT_CARD')]}),

    ("Notification sent to jjg36@gmail.com.",
     {"entities": [(21, 36, 'EMAIL')]}),

    ("Property located at Renuka complex, Raghav Nagar, Deoria, Uttar Pradesh 274001.",
     {"entities": [(20, 78, 'ADDRESS')]}),

    ("Card 4503778880156607 linked to j_i4z1t8@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 50, 'EMAIL')]}),

    ("Email p2gso_mpi@gmail.com not verified.",
     {"entities": [(6, 25, 'EMAIL')]}),

    ("New card 5119998465235916 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Customer lives at 9HVP+H48, Sadhwara St, Manhari, Farrukhabad, Uttar Pradesh 209625.",
     {"entities": [(18, 83, 'ADDRESS')]}),

    ("Kiran Bedi card 379109685250555 blocked.",
     {"entities": [(0, 10, 'PERSON'), (16, 31, 'CREDIT_CARD')]}),

    ("Payment failed for card 4421907374387770.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Please contact y5zxyoj.kj1.phajwo@gmail.com for queries.",
     {"entities": [(15, 43, 'EMAIL')]}),

    ("Send statement to eb_b6kfro3_02iuy99@gmail.com for Vikram Malhotra.",
     {"entities": [(18, 46, 'EMAIL'), (51, 66, 'PERSON')]}),

    ("Email x_vc78d@gmail.com not verified.",
     {"entities": [(6, 23, 'EMAIL')]}),

    ("User registered with v.236edk6jo.rqnd0hp@gmail.com.",
     {"entities": [(21, 50, 'EMAIL')]}),

    ("Customer lives at Ground Floor Part of Khasra No 294,295& 298, Mohalla Nawada Shekhan.",
     {"entities": [(18, 85, 'ADDRESS')]}),

    ("Charge card number 6015724525299546 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("OTP sent to wwdyeqh6fse@gmail.com.",
     {"entities": [(12, 33, 'EMAIL')]}),

    ("Customer Meena Patel lives at Jaina holidays, 22a, Gher Khatti, New Mandi, Muzaffarnagar. Contact: f2_2iv8gzgjmmdfy@gmail.com.",
     {"entities": [(9, 20, 'PERSON'), (30, 88, 'ADDRESS'), (99, 125, 'EMAIL')]}),

    ("Transaction on card 5172359055319435 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("User registered with cggfpkjo6aa6@gmail.com.",
     {"entities": [(21, 43, 'EMAIL')]}),

    ("Card 345070621748936 linked to frizwue@gmail.com.",
     {"entities": [(5, 20, 'CREDIT_CARD'), (31, 48, 'EMAIL')]}),

    ("Delivery address is Level 1, Southern Park, A- Wing, Pamposh Enclave, District Centre.",
     {"entities": [(20, 85, 'ADDRESS')]}),

    ("Statement sent to hgjws2as@gmail.com successfully.",
     {"entities": [(18, 36, 'EMAIL')]}),

    ("Vikram Malhotra at CG9G+XF6 Gautam Buddha University, Yamuna Expy, Greater Noida, email yxq_ndwn.3mtxgmw_1@gmail.com.",
     {"entities": [(0, 15, 'PERSON'), (19, 80, 'ADDRESS'), (88, 116, 'EMAIL')]}),

    ("Verify card 5198989004906436 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Please contact l61nejsy2v1q@gmail.com for queries.",
     {"entities": [(15, 37, 'EMAIL')]}),

    ("OTP sent to unphzmt6@gmail.com.",
     {"entities": [(12, 30, 'EMAIL')]}),

    ("Send report to q0vat@gmail.com.",
     {"entities": [(15, 30, 'EMAIL')]}),

    ("Verify card 4634839779893516 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Notification sent to oqw0um96hfrje4b@gmail.com.",
     {"entities": [(21, 46, 'EMAIL')]}),

    ("Email g50rmptz3ehcv08d0@gmail.com not verified.",
     {"entities": [(6, 33, 'EMAIL')]}),

    ("Disputed transaction on card 347909142593062.",
     {"entities": [(29, 44, 'CREDIT_CARD')]}),

    ("Customer Kiran Bedi lives at 3, 10, Block 3, East Patel Nagar, Patel Nagar, New Delhi, Delhi 110008. Contact: l5ezkz2h@gmail.com.",
     {"entities": [(9, 19, 'PERSON'), (29, 99, 'ADDRESS'), (110, 128, 'EMAIL')]}),

    ("Charge card number 6578226180832720 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Payment failed for card 5234996071269080.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Office is at F-300, Block FB, Mansarover Garden, Delhi, 110015.",
     {"entities": [(13, 62, 'ADDRESS')]}),

    ("Kiran Bedi at Asthbuji Colony, Bari Bagh, Lanka, Ghazipur, Uttar Pradesh 233001, email wuyiz2e4z2@gmail.com.",
     {"entities": [(0, 10, 'PERSON'), (14, 79, 'ADDRESS'), (87, 107, 'EMAIL')]}),

    ("New card 343536283841440 issued to customer.",
     {"entities": [(9, 24, 'CREDIT_CARD')]}),

    ("Delivery address is 51, GHOORAN TALAIYA, Char Khamba, Rang Mahla, Shahjahanpur.",
     {"entities": [(20, 78, 'ADDRESS')]}),

    ("Send documents to 832W+PQJ, Naugarh Bypass Rd, Birdpur No.14, Naugarh, Uttar Pradesh 272203.",
     {"entities": [(18, 91, 'ADDRESS')]}),

    ("Please ship to CV38+M2F, Upper Kot, Bulandshahr, Uttar Pradesh 203001.",
     {"entities": [(15, 69, 'ADDRESS')]}),

    ("Office is at Hzhhf, Abc, NCR, South Extension I, Trilok Colony, Region, New Delhi.",
     {"entities": [(13, 81, 'ADDRESS')]}),

    ("Email mfgtls.l@gmail.com not verified.",
     {"entities": [(6, 24, 'EMAIL')]}),

    ("Account linked to nhbborjoep81trgbcl8@gmail.com.",
     {"entities": [(18, 47, 'EMAIL')]}),

    ("Invoice to be sent at 48MQ+JJX, Avas Vikas, Jalaun, Uttar Pradesh 285123.",
     {"entities": [(22, 72, 'ADDRESS')]}),

    ("Disputed transaction on card 5127660279186714.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Notification sent to zz0hf@gmail.com.",
     {"entities": [(21, 36, 'EMAIL')]}),

    ("Branch office at 353P+MPG, Sikhpur, Azamgarh, Uttar Pradesh 276001.",
     {"entities": [(17, 66, 'ADDRESS')]}),

    ("User registered with hl1fljoi6@gmail.com.",
     {"entities": [(21, 40, 'EMAIL')]}),

    ("Branch office at Housing Colony, Gonda, Uttar Pradesh 271003, Gonda, Uttar Pradesh 271003.",
     {"entities": [(17, 89, 'ADDRESS')]}),

    ("Notification sent to st2lk3df_jqy3wu4@gmail.com.",
     {"entities": [(21, 47, 'EMAIL')]}),

    ("Property located at Railway Station, Road, Khalilabad, Uttar Pradesh 272175.",
     {"entities": [(20, 75, 'ADDRESS')]}),

    ("Block card 6018498024548147 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Statement sent to eg7kha2@gmail.com successfully.",
     {"entities": [(18, 35, 'EMAIL')]}),

    ("Invoice to be sent at Vinayak Central Plaza, near Big Bazar, Civil Lines, Prayagraj.",
     {"entities": [(22, 83, 'ADDRESS')]}),

    ("OTP sent to yhv22@gmail.com.",
     {"entities": [(12, 27, 'EMAIL')]}),

    ("Account linked to bsmxkz5rd2epus.vwpl@gmail.com.",
     {"entities": [(18, 47, 'EMAIL')]}),

    ("Customer Suresh Patel lives at Q2PC+W83, Avas Vikas Rd, Gangapur Avas Vikas, Civil Lines, Rampur. Contact: zembf5_kag4@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 96, 'ADDRESS'), (107, 128, 'EMAIL')]}),

    ("Property located at PH-I S.O, PANKAJ GRAND PLAZA, CSC, Mayur Vihar, Delhi 110091.",
     {"entities": [(20, 80, 'ADDRESS')]}),

    ("Please ship to R925+24F, Vikas Nagar Awasivya Colony, Vistar Colony, Gorakhpur.",
     {"entities": [(15, 78, 'ADDRESS')]}),

    ("Send report to nkkbhx80qgonp_e8.l@gmail.com.",
     {"entities": [(15, 43, 'EMAIL')]}),

    ("Verify card 6032609472370504 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Invoice to be sent at pocket -4&5, 72, Sector 23, Rohini, New Delhi, Delhi 110085.",
     {"entities": [(22, 81, 'ADDRESS')]}),

    ("Customer lives at 26WH+F8M, Jamuri Shahgarh, Azamgarh, Uttar Pradesh 276406.",
     {"entities": [(18, 75, 'ADDRESS')]}),

    ("Send documents to WW9F+4QR, Chinnor, Shahjahanpur, Shahjhanpur North, Uttar Pradesh 242001.",
     {"entities": [(18, 90, 'ADDRESS')]}),

    ("Verify card 340903702463050 with bank.",
     {"entities": [(12, 27, 'CREDIT_CARD')]}),

    ("Sanjay Gupta at C/2-207 Block, Block C 2, Block C, New Ashok Nagar, Delhi, 110096, email yamtde4y8zcenr58f@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 81, 'ADDRESS'), (89, 116, 'EMAIL')]}),

    ("Payment failed for card 5375556729737578.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Suresh Patel used card 5390951158770476 at PV9G+R74, Mangalpur, Uttar Pradesh 274206.",
     {"entities": [(0, 12, 'PERSON'), (23, 39, 'CREDIT_CARD'), (43, 84, 'ADDRESS')]}),

    ("Bill sent to ssd3bc@gmail.com for card 4799466597099755.",
     {"entities": [(13, 29, 'EMAIL'), (39, 55, 'CREDIT_CARD')]}),

    ("Card 6539202156403572 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Please ship to HHMP+9W7, Salarganj, Gulamali Pura, Bahraich, Uttar Pradesh 271801.",
     {"entities": [(15, 81, 'ADDRESS')]}),

    ("Billing address: 4XQX+MMM, Defence Colony, Agra, Uttar Pradesh 282001.",
     {"entities": [(17, 69, 'ADDRESS')]}),

    ("Block card 4892652047078703 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Send OTP to zj3.tv@gmail.com immediately.",
     {"entities": [(12, 28, 'EMAIL')]}),

    ("User registered with wr06ssjzi8@gmail.com.",
     {"entities": [(21, 41, 'EMAIL')]}),

    ("Account linked to lb1221@gmail.com.",
     {"entities": [(18, 34, 'EMAIL')]}),

    ("Invoice to be sent at Chakrapanpur, Uttar Pradesh 276128.",
     {"entities": [(22, 56, 'ADDRESS')]}),

    ("Office is at C997+7JR LIC Colony Park, Defence Colony, Shyam Nagar, Kanpur.",
     {"entities": [(13, 74, 'ADDRESS')]}),

    ("Registered address: HHF9+V96, Kacheri, Ghazipur, Uttar Pradesh 233001.",
     {"entities": [(20, 69, 'ADDRESS')]}),

    ("Account linked to he9ncz9ez@gmail.com.",
     {"entities": [(18, 37, 'EMAIL')]}),

    ("Neha Joshi at 5H26+84W, Narghat, Gosain Tola, Mirzapur-cum-Vindhyachal, Mirzapur, email sahvruhb6aunabw82@gmail.com.",
     {"entities": [(0, 10, 'PERSON'), (14, 80, 'ADDRESS'), (88, 115, 'EMAIL')]}),

    ("Recovery email set to j0_6k.sfb@gmail.com.",
     {"entities": [(22, 41, 'EMAIL')]}),

    ("Send OTP to a1steokdio5ux72z3yah@gmail.com immediately.",
     {"entities": [(12, 42, 'EMAIL')]}),

    ("Charge card number 6029604252298687 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Send statement to qpve9_n68ock87@gmail.com for Sunita Verma.",
     {"entities": [(18, 42, 'EMAIL'), (47, 59, 'PERSON')]}),

    ("Charge card number 347768800697690 for INR 2000.",
     {"entities": [(19, 34, 'CREDIT_CARD')]}),

    ("Please ship to BHORANJ TEHSIL-BHORANJ, DISTT, Hamirpur, Himachal Pradesh 177601.",
     {"entities": [(15, 79, 'ADDRESS')]}),

    ("User registered with clpbhzdt71ap5@gmail.com.",
     {"entities": [(21, 44, 'EMAIL')]}),

    ("Block card 377909705548625 immediately.",
     {"entities": [(11, 26, 'CREDIT_CARD')]}),

    ("Delivery address is Shahpur, Gorakhpur, Uttar Pradesh 273001.",
     {"entities": [(20, 60, 'ADDRESS')]}),

    ("New card 5479330183917548 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Delivery address is WHV9+9VF, Bulaki Pura, Mau, Uttar Pradesh 275101.",
     {"entities": [(20, 68, 'ADDRESS')]}),

    ("Account linked to fn02o.ito@gmail.com.",
     {"entities": [(18, 37, 'EMAIL')]}),

    ("Account linked to uej6uz.uyt3@gmail.com.",
     {"entities": [(18, 39, 'EMAIL')]}),

    ("Registered address: Upper & Lower Ground Floor, Alex Tower, Farenda Road, near Shyam Mandir.",
     {"entities": [(20, 91, 'ADDRESS')]}),

    ("Bill sent to ifq0g1ecmjm4ndqk@gmail.com for card 4214346754306766.",
     {"entities": [(13, 39, 'EMAIL'), (49, 65, 'CREDIT_CARD')]}),

    ("Card 370550079641506 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("New card 342599023774923 issued to customer.",
     {"entities": [(9, 24, 'CREDIT_CARD')]}),

    ("Delivery address is Block A Rd, Block A, Surya Nagar, Delhi, Ghaziabad, Uttar Pradesh 201011.",
     {"entities": [(20, 92, 'ADDRESS')]}),

    ("Send OTP to istes4pfu@gmail.com immediately.",
     {"entities": [(12, 31, 'EMAIL')]}),

    ("Branch office at 49WQ+5W5, Sanjay Singh Colony, Om Nagar Colony, Firozabad.",
     {"entities": [(17, 74, 'ADDRESS')]}),

    ("Ananya Krishnamurthy card 373926229499128 blocked.",
     {"entities": [(0, 20, 'PERSON'), (26, 41, 'CREDIT_CARD')]}),

    ("Billing address: No 4/1459, Ground Floor, Safina Complex, Medical Road, Phase 1.",
     {"entities": [(17, 79, 'ADDRESS')]}),

    ("Card 4916316181025348 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Send statement to hm_frk1ru4sveny6d3@gmail.com for Priya Singh.",
     {"entities": [(18, 46, 'EMAIL'), (51, 62, 'PERSON')]}),

    ("OTP sent to yku85ai_5yom8q@gmail.com.",
     {"entities": [(12, 36, 'EMAIL')]}),

    ("Registered address: Near Tvs Agency Esan nadi crossing bhogaon, Road, Mainpuri.",
     {"entities": [(20, 78, 'ADDRESS')]}),

    ("Recovery email set to wpsb3i0y@gmail.com.",
     {"entities": [(22, 40, 'EMAIL')]}),

    ("Branch office at Q29J+5GW, M.S. Nagar, Ekta Colony, Etawah, Uttar Pradesh 206001.",
     {"entities": [(17, 80, 'ADDRESS')]}),

    ("Account linked to v6h5zfqwxxvy0l@gmail.com.",
     {"entities": [(18, 42, 'EMAIL')]}),

    ("Delivery address is W32M+9CM, Amir Nishan, Aligarh, Uttar Pradesh 202001.",
     {"entities": [(20, 72, 'ADDRESS')]}),

    ("Recovery email set to nx5gaa@gmail.com.",
     {"entities": [(22, 38, 'EMAIL')]}),

    ("Branch office at Shop No.201-204, MSX TOWER-2, 01, Sector Alpha Rd, Alpha-I Commercial Belt.",
     {"entities": [(17, 91, 'ADDRESS')]}),

    ("Send OTP to sspsv@gmail.com immediately.",
     {"entities": [(12, 27, 'EMAIL')]}),

    ("Billing address: W5HR+69V, Begum Gunj, Barabanki, Uttar Pradesh 225001.",
     {"entities": [(17, 70, 'ADDRESS')]}),

    ("Office is at 53/45, Patel Nagar Rd, Canal Colony, Civil Lines, Fatehpur.",
     {"entities": [(13, 71, 'ADDRESS')]}),

    ("Account linked to l7i_6yo9w.hafedry_8@gmail.com.",
     {"entities": [(18, 47, 'EMAIL')]}),

    ("Notification sent to a5qwwez03fr3@gmail.com.",
     {"entities": [(21, 43, 'EMAIL')]}),

    ("Please contact rl4ifq6sypszl@gmail.com for queries.",
     {"entities": [(15, 38, 'EMAIL')]}),

    ("Notification sent to u3emw@gmail.com.",
     {"entities": [(21, 36, 'EMAIL')]}),

    ("Please contact zzq0.gmybz@gmail.com for queries.",
     {"entities": [(15, 35, 'EMAIL')]}),

    ("Vikram Malhotra at 669V+W22, Kutchery Rd, Nirala Nagar, Raebareli, Uttar Pradesh 229001, email a32r7n.r@gmail.com.",
     {"entities": [(0, 15, 'PERSON'), (19, 87, 'ADDRESS'), (95, 113, 'EMAIL')]}),

    ("Delivery address is 5G22+MJG, Kantit, Vindhyachal, Mirzapur, Uttar Pradesh 231307.",
     {"entities": [(20, 81, 'ADDRESS')]}),

    ("Account linked to hn1elceavuw@gmail.com.",
     {"entities": [(18, 39, 'EMAIL')]}),

    ("Card 4311700496317035 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Billing address: Kakrahi, Hardoi Road, SH 25, Hardoi, Uttar Pradesh 241001.",
     {"entities": [(17, 74, 'ADDRESS')]}),

    ("Branch office at Gas Agency Road, Shadipur Chauraha, Fatehpur, Uttar Pradesh 212665.",
     {"entities": [(17, 83, 'ADDRESS')]}),

    ("Pallavi Joshi used card 4202617893050352 at 9CRH+83W, Mini Byp, vrindavan Colony, Rajendra Nagar, Bareilly.",
     {"entities": [(0, 13, 'PERSON'), (24, 40, 'CREDIT_CARD'), (44, 106, 'ADDRESS')]}),

    ("Notification sent to z4_8pjw0bwi2fert@gmail.com.",
     {"entities": [(21, 47, 'EMAIL')]}),

    ("Card 6024912745019372 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Send documents to Old Katra, Prayagraj, Uttar Pradesh 211002.",
     {"entities": [(18, 60, 'ADDRESS')]}),

    ("Geeta Rani card 4591515699465670 blocked.",
     {"entities": [(0, 10, 'PERSON'), (16, 32, 'CREDIT_CARD')]}),

    ("Card 4135433247937235 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Bill sent to s02e79rpe@gmail.com for card 348019522404892.",
     {"entities": [(13, 32, 'EMAIL'), (42, 57, 'CREDIT_CARD')]}),

    ("Property located at FF5W+HJC, Gursahaiganj - Jalaun Rd, Tilak Nagar, Auraiya.",
     {"entities": [(20, 76, 'ADDRESS')]}),

    ("Ananya Krishnamurthy card 343322228716571 blocked.",
     {"entities": [(0, 20, 'PERSON'), (26, 41, 'CREDIT_CARD')]}),

    ("Verify card 5276777565703934 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("New card 6589087954760042 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Payment failed for card 6569768378757923.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Card 5190326711558604 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Customer Pallavi Joshi lives at Station Rd, Ballabh Nagar Colony, Pilibhit, Uttar Pradesh 262001. Contact: he0j4csgs@gmail.com.",
     {"entities": [(9, 22, 'PERSON'), (32, 96, 'ADDRESS'), (107, 126, 'EMAIL')]}),

    ("OTP sent to lqy0bkm2eaa@gmail.com.",
     {"entities": [(12, 33, 'EMAIL')]}),

    ("New card 4662103332959147 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Transaction on card 6502663233095619 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Office is at Sonari Chauraha, Post Haisar Bazar, Shiv Mandir Road, Khalilabad, Ghorang.",
     {"entities": [(13, 86, 'ADDRESS')]}),

    ("Verify card 379183738990851 with bank.",
     {"entities": [(12, 27, 'CREDIT_CARD')]}),

    ("Send report to l2h1e4076bkriscb@gmail.com.",
     {"entities": [(15, 41, 'EMAIL')]}),

    ("Send OTP to ce09xv@gmail.com immediately.",
     {"entities": [(12, 28, 'EMAIL')]}),

    ("Nisha Agarwal used card 5352836202192292 at Umarpur, polytechnic chauraha, Jaunpur, Uttar Pradesh 222002.",
     {"entities": [(0, 13, 'PERSON'), (24, 40, 'CREDIT_CARD'), (44, 104, 'ADDRESS')]}),

    ("Transaction on card 6595732561802079 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Notification sent to ec3op@gmail.com.",
     {"entities": [(21, 36, 'EMAIL')]}),

    ("Rohit Mehta card 5366374959405229 blocked.",
     {"entities": [(0, 11, 'PERSON'), (17, 33, 'CREDIT_CARD')]}),

    ("Send statement to m68xcsupcc@gmail.com for Sunita Verma.",
     {"entities": [(18, 38, 'EMAIL'), (43, 55, 'PERSON')]}),

    ("Customer Sanjay Gupta lives at 77C6+RGQ, Sakaldiha - Chandauli Rd, near polytechnic college, Danpur. Contact: c.pf.n_t3@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 99, 'ADDRESS'), (110, 129, 'EMAIL')]}),

    ("Verify card 4978629574288926 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Bill sent to lfqyg8oiz6wal4z2w@gmail.com for card 377350571705986.",
     {"entities": [(13, 40, 'EMAIL'), (50, 65, 'CREDIT_CARD')]}),

    ("Transaction on card 374108950030413 was declined.",
     {"entities": [(20, 35, 'CREDIT_CARD')]}),

    ("Customer Kiran Bedi lives at S-571, Inder Mohan Bhardwaj Marg, Block S, Greater Kailash II, Alaknanda. Contact: mlxdksjbjzxne.w@gmail.com.",
     {"entities": [(9, 19, 'PERSON'), (29, 101, 'ADDRESS'), (112, 137, 'EMAIL')]}),

    ("Account linked to h3330k0_ue@gmail.com.",
     {"entities": [(18, 38, 'EMAIL')]}),

    ("Block card 4529244553142599 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Payment failed for card 6509977272846626.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Card 6510373694714688 linked to fat9iw3r9pf2@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 54, 'EMAIL')]}),

    ("Please ship to Etah, Shitalpur, Uttar Pradesh 207121.",
     {"entities": [(15, 52, 'ADDRESS')]}),

    ("Account linked to ehgxx7@gmail.com.",
     {"entities": [(18, 34, 'EMAIL')]}),

    ("Bill sent to tnpux74ck4yzer7d@gmail.com for card 6591446998488114.",
     {"entities": [(13, 39, 'EMAIL'), (49, 65, 'CREDIT_CARD')]}),

    ("Recovery email set to nkjxvko2qr5k64jd9@gmail.com.",
     {"entities": [(22, 49, 'EMAIL')]}),

    ("Customer lives at 206, KATRA SEWA KALI, Kabirganj, Etawah, Uttar Pradesh 206001.",
     {"entities": [(18, 79, 'ADDRESS')]}),

    ("Send statement to i2olo07023@gmail.com for Ananya Krishnamurthy.",
     {"entities": [(18, 38, 'EMAIL'), (43, 63, 'PERSON')]}),

    ("Customer lives at Shop No 1 Karhal Crossing Bypass, Road, Station Road, Mainpuri.",
     {"entities": [(18, 80, 'ADDRESS')]}),

    ("Charge card number 6526485184697551 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Please ship to Mahindra Agency, Tanda Road, Gali, Bahavddihpur, Ravi Pur, Akbarpur.",
     {"entities": [(15, 82, 'ADDRESS')]}),

    ("Shruti Desai at Kotwali Rd, Tularam, Puranpur, Pilibhit, Uttar Pradesh 262122, email bm087snrfxgc9@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 77, 'ADDRESS'), (85, 108, 'EMAIL')]}),

    ("Invoice to be sent at Jila Mainpuri Mota road, Bewar road, Hasanpur, Uttar Pradesh 205262.",
     {"entities": [(22, 89, 'ADDRESS')]}),

    ("Billing address: B 49 Mehtab Complex, I.P. EXTENTION, Patpar Ganj, Joshi Colony, Mandawli.",
     {"entities": [(17, 89, 'ADDRESS')]}),

    ("Registered address: Tirwa Rd, near UCO bank, Akbarpur Maj, Kannauj, Uttar Pradesh 209727.",
     {"entities": [(20, 88, 'ADDRESS')]}),

    ("Property located at Ground Floor, Double Fatak Road, near ICICI ATM, Sanjay Nagar, Faiz Ganj.",
     {"entities": [(20, 92, 'ADDRESS')]}),

    ("Disputed transaction on card 342107719145447.",
     {"entities": [(29, 44, 'CREDIT_CARD')]}),

    ("Send OTP to f10tkq3e3hx@gmail.com immediately.",
     {"entities": [(12, 33, 'EMAIL')]}),

    ("Card 4419828352791651 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Charge card number 376912846262354 for INR 2000.",
     {"entities": [(19, 34, 'CREDIT_CARD')]}),

    ("Delivery address is 6WFC+P7J, Talib City, Chitrakoot Dham, Uttar Pradesh 210205.",
     {"entities": [(20, 79, 'ADDRESS')]}),

    ("Sanjay Gupta card 344754675417047 blocked.",
     {"entities": [(0, 12, 'PERSON'), (18, 33, 'CREDIT_CARD')]}),

    ("Please ship to G23P+CH8, Shravasti, Khargupur, Uttar Pradesh 271805.",
     {"entities": [(15, 67, 'ADDRESS')]}),

    ("Send statement to i7qvbvccwk.l6ej@gmail.com for Shruti Desai.",
     {"entities": [(18, 43, 'EMAIL'), (48, 60, 'PERSON')]}),

    ("Billing address: Hanumat dham, Near, Bisrat Road, Hussain Pura, Shahjahanpur.",
     {"entities": [(17, 76, 'ADDRESS')]}),

    ("Transaction on card 4956973060992370 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Bill sent to s733073@gmail.com for card 6507901906629646.",
     {"entities": [(13, 30, 'EMAIL'), (40, 56, 'CREDIT_CARD')]}),

    ("Priya Singh card 5412414298506714 blocked.",
     {"entities": [(0, 11, 'PERSON'), (17, 33, 'CREDIT_CARD')]}),

    ("Card 346030988280818 linked to yx2jam@gmail.com.",
     {"entities": [(5, 20, 'CREDIT_CARD'), (31, 47, 'EMAIL')]}),

    ("Card 6523432876977167 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("New card 5142268369759678 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("User registered with ubf2i1sj@gmail.com.",
     {"entities": [(21, 39, 'EMAIL')]}),

    ("Statement sent to opf.hzsts4@gmail.com successfully.",
     {"entities": [(18, 38, 'EMAIL')]}),

    ("New card 5528160529953153 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Bill sent to oeeq2ok.lwv@gmail.com for card 4342768922914794.",
     {"entities": [(13, 34, 'EMAIL'), (44, 60, 'CREDIT_CARD')]}),

    ("Payment failed for card 5146993563371322.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Send report to c1oaa_z0l4fyom.mp@gmail.com.",
     {"entities": [(15, 42, 'EMAIL')]}),

    ("Registered address: SHOP NO, NEARTARAWATI HOSPITAL, 1, Bajoria Rd, Janak Nagar, Saharanpur.",
     {"entities": [(20, 90, 'ADDRESS')]}),

    ("Notification sent to sya0k7woy5tk9e74e@gmail.com.",
     {"entities": [(21, 48, 'EMAIL')]}),

    ("Email s4tek47jlk@gmail.com not verified.",
     {"entities": [(6, 26, 'EMAIL')]}),

    ("New card 341654997580060 issued to customer.",
     {"entities": [(9, 24, 'CREDIT_CARD')]}),

    ("Office is at M637+FF5, Church Rd, Nabi Karim, Sadar Bazaar, New Delhi, Delhi, 110055.",
     {"entities": [(13, 84, 'ADDRESS')]}),

    ("Statement sent to ylza4.ijjw60@gmail.com successfully.",
     {"entities": [(18, 40, 'EMAIL')]}),

    ("Send report to ef4abvimmg6@gmail.com.",
     {"entities": [(15, 36, 'EMAIL')]}),

    ("Branch office at Plot no 11, Block A, Sector 12 Dwarka, Dwarka, Delhi, 110078.",
     {"entities": [(17, 77, 'ADDRESS')]}),

    ("Card 4248036355927593 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Office is at Khasra No 579, GF&, MF, Abadi, Meerut Rd, near Munnalal Enclave.",
     {"entities": [(13, 76, 'ADDRESS')]}),

    ("User registered with giy6x_y.gixoeh_s2j3@gmail.com.",
     {"entities": [(21, 50, 'EMAIL')]}),

    ("Email lr2y0urzeoi@gmail.com not verified.",
     {"entities": [(6, 27, 'EMAIL')]}),

    ("Notification sent to jtig8vyaccafysiil@gmail.com.",
     {"entities": [(21, 48, 'EMAIL')]}),

    ("Block card 6079228414530714 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Nisha Agarwal card 344270766797127 blocked.",
     {"entities": [(0, 13, 'PERSON'), (19, 34, 'CREDIT_CARD')]}),

    ("Registered address: on Amarnath Properties, near Majhola Road, Prakash Nagar, Chiriya Tola.",
     {"entities": [(20, 90, 'ADDRESS')]}),

    ("Verify card 6039645128558046 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Office is at Agriculture Colony, Hamirpur, Himachal Pradesh 177001.",
     {"entities": [(13, 66, 'ADDRESS')]}),

    ("Verify card 5497839670752733 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Send documents to Beliganj Rd, PNT Colony, Raebareli, Uttar Pradesh 229001.",
     {"entities": [(18, 74, 'ADDRESS')]}),

    ("Card 340758232626488 was used at ATM.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Please contact mbpo6oz8kbtc01lj@gmail.com for queries.",
     {"entities": [(15, 41, 'EMAIL')]}),

    ("Disputed transaction on card 5357809910364577.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Account linked to is_qkv7u21zj48i@gmail.com.",
     {"entities": [(18, 43, 'EMAIL')]}),

    ("Sunita Verma used card 372785378990654 at Bijnor - Moradabad Road, Village, near Dharampura, Bijnor.",
     {"entities": [(0, 12, 'PERSON'), (23, 38, 'CREDIT_CARD'), (42, 99, 'ADDRESS')]}),

    ("Property located at Link Road, Chiranjeevi Palace, infront of Ganga Computers.",
     {"entities": [(20, 77, 'ADDRESS')]}),

    ("Invoice to be sent at No. 30, 49, Chhipitola, Rakabganj, Agra, Uttar Pradesh 282001.",
     {"entities": [(22, 83, 'ADDRESS')]}),

    ("Recovery email set to ao5nomdetg5llkb8imhf@gmail.com.",
     {"entities": [(22, 52, 'EMAIL')]}),

    ("Delivery address is Q93J+2FR, Gorakhpur University Road, Kawwa Bagh Colony, Gorakhpur.",
     {"entities": [(20, 85, 'ADDRESS')]}),

    ("Customer Kiran Bedi lives at 341/148/2D, Chakiya, Rajrooppur, Prayagraj, Uttar Pradesh 211016. Contact: daet.5wpi7otv@gmail.com.",
     {"entities": [(9, 19, 'PERSON'), (29, 93, 'ADDRESS'), (104, 127, 'EMAIL')]}),

    ("Card 4699724091093327 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Please contact pmpfxu78fm_xnaea9@gmail.com for queries.",
     {"entities": [(15, 42, 'EMAIL')]}),

    ("Billing address: Aalamgiri Masjid, Quila Bazar, Quziyana Quila, Raebareli.",
     {"entities": [(17, 73, 'ADDRESS')]}),

    ("Customer Rohit Mehta lives at 63H5+66C, Niranjanpur, Bhojpura, Mainpuri, Uttar Pradesh 205001. Contact: qbxov13uz5xp@gmail.com.",
     {"entities": [(9, 20, 'PERSON'), (30, 93, 'ADDRESS'), (104, 126, 'EMAIL')]}),

    ("Billing address: 5th Floor, Gaur Central Mall, opposite HDFC Bank, RDC, Block 1.",
     {"entities": [(17, 79, 'ADDRESS')]}),

    ("Email rqwvq0z7s1a3h0ckdb@gmail.com not verified.",
     {"entities": [(6, 34, 'EMAIL')]}),

    ("Bill sent to r7unrfe99i@gmail.com for card 6561439665302111.",
     {"entities": [(13, 33, 'EMAIL'), (43, 59, 'CREDIT_CARD')]}),

    ("Payment failed for card 344705510534057.",
     {"entities": [(24, 39, 'CREDIT_CARD')]}),

    ("Recovery email set to sn_pkkovktn@gmail.com.",
     {"entities": [(22, 43, 'EMAIL')]}),

    ("Please ship to Rahul Nagar Marya, Marhaya, Azamgarh, Uttar Pradesh 276001.",
     {"entities": [(15, 73, 'ADDRESS')]}),

    ("Bill sent to vxp5.e94xwq4txams@gmail.com for card 5469697085773620.",
     {"entities": [(13, 40, 'EMAIL'), (50, 66, 'CREDIT_CARD')]}),

    ("Customer Priya Singh lives at Shahadara Drain New Delhi, Delhi, Uttar Pradesh 110001. Contact: fkv9atkk9t@gmail.com.",
     {"entities": [(9, 20, 'PERSON'), (30, 84, 'ADDRESS'), (95, 115, 'EMAIL')]}),

    ("Please contact xai38flnc@gmail.com for queries.",
     {"entities": [(15, 34, 'EMAIL')]}),

    ("Send statement to z85qm@gmail.com for Amit Kumar.",
     {"entities": [(18, 33, 'EMAIL'), (38, 48, 'PERSON')]}),

    ("Property located at PMWF+2W, Tarapur Colony, Olandganj, Jaunpur, Uttar Pradesh 222002.",
     {"entities": [(20, 85, 'ADDRESS')]}),

    ("New card 5460108978479035 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Notification sent to r56vhu@gmail.com.",
     {"entities": [(21, 37, 'EMAIL')]}),

    ("Block card 373108722585528 immediately.",
     {"entities": [(11, 26, 'CREDIT_CARD')]}),

    ("Rohit Mehta used card 4597329220033068 at Ground-First Floor, Pilikothi, Chawni, beside Kundan's Restaurant.",
     {"entities": [(0, 11, 'PERSON'), (22, 38, 'CREDIT_CARD'), (42, 107, 'ADDRESS')]}),

    ("Billing address: Grand Trunk Rd, New Tika Ram Colony, Mukund Nagar, Naurangabad, Aligarh.",
     {"entities": [(17, 88, 'ADDRESS')]}),

    ("User registered with tnrm1zhieyz._oc@gmail.com.",
     {"entities": [(21, 46, 'EMAIL')]}),

    ("Verify card 5222877759118726 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Statement sent to mnm2r5_ffm5eto1fi.d8@gmail.com successfully.",
     {"entities": [(18, 48, 'EMAIL')]}),

    ("Send OTP to ftxqlnywf83vk@gmail.com immediately.",
     {"entities": [(12, 35, 'EMAIL')]}),

    ("Send OTP to qct0_6mslj6s@gmail.com immediately.",
     {"entities": [(12, 34, 'EMAIL')]}),

    ("Charge card number 5198796865494313 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Registered address: MQHH+V8M, Rasulabad, Uttar Pradesh 209306.",
     {"entities": [(20, 61, 'ADDRESS')]}),

    ("Property located at PWV9+R23, cantt, Babugarh, Kuchesar Road Chaupala, Uttar Pradesh 245201.",
     {"entities": [(20, 91, 'ADDRESS')]}),

    ("Disputed transaction on card 4866661409707579.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("New card 5219327377301783 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Send OTP to gd0kejzo6wz8zs9ve@gmail.com immediately.",
     {"entities": [(12, 39, 'EMAIL')]}),

    ("Neha Joshi card 5172627342282069 blocked.",
     {"entities": [(0, 10, 'PERSON'), (16, 32, 'CREDIT_CARD')]}),

    ("Notification sent to p9k6dzq5_ywsudb_cixw@gmail.com.",
     {"entities": [(21, 51, 'EMAIL')]}),

    ("Delivery address is Kazakpur Colony, Bhagat Chauraha, near parwati marriage hall, Taramandal.",
     {"entities": [(20, 92, 'ADDRESS')]}),

    ("Branch office at HM57+VGM, Babuganj, Etah, Uttar Pradesh 207001.",
     {"entities": [(17, 63, 'ADDRESS')]}),

    ("Kiran Bedi at Q564+3Q9, Satish Chandra College,, NH 19, Bahadurpur, Ballia, email xwtv6z5z84bqg.5h9382@gmail.com.",
     {"entities": [(0, 10, 'PERSON'), (14, 74, 'ADDRESS'), (82, 112, 'EMAIL')]}),

    ("Notification sent to fy6f42mrkusw@gmail.com.",
     {"entities": [(21, 43, 'EMAIL')]}),

    ("Card 342915744405631 was used at ATM.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Send statement to qa.10pa.uz4xudm2@gmail.com for Vikram Malhotra.",
     {"entities": [(18, 44, 'EMAIL'), (49, 64, 'PERSON')]}),

    ("Send OTP to d2vab_lzg_8wh9g2@gmail.com immediately.",
     {"entities": [(12, 38, 'EMAIL')]}),

    ("Customer lives at W6J2+J5W, Unnamed Road, Choudary Nagar, Barabanki, Uttar Pradesh 225001.",
     {"entities": [(18, 89, 'ADDRESS')]}),

    ("Disputed transaction on card 346629522104064.",
     {"entities": [(29, 44, 'CREDIT_CARD')]}),

    ("Send report to jt8id551@gmail.com.",
     {"entities": [(15, 33, 'EMAIL')]}),

    ("Office is at 1/2049, Priya Apartments, Durga Mandir Marg, Ram Nagar, Shahdara, Delhi.",
     {"entities": [(13, 84, 'ADDRESS')]}),

    ("Email g2d2de@gmail.com not verified.",
     {"entities": [(6, 22, 'EMAIL')]}),

    ("Account linked to l8bizj@gmail.com.",
     {"entities": [(18, 34, 'EMAIL')]}),

    ("Customer Rohit Mehta lives at Kalwati Gatta Market, Kacheri Tola, near by:Bake Well, Safdarganj, Kannauj. Contact: n2indv3ulgnh7y@gmail.com.",
     {"entities": [(9, 20, 'PERSON'), (30, 104, 'ADDRESS'), (115, 139, 'EMAIL')]}),

    ("Card 4330584682820349 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Statement sent to yx637ckc_dfx@gmail.com successfully.",
     {"entities": [(18, 40, 'EMAIL')]}),

    ("Card 4484662608573213 linked to pz6fzju.shrt@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 54, 'EMAIL')]}),

    ("Customer lives at Shaheed Smarak Road, Piprouli, Basantpur, Uttar Pradesh 277301.",
     {"entities": [(18, 80, 'ADDRESS')]}),

    ("Customer lives at Baradari, Katra, Barabanki, Uttar Pradesh 225001.",
     {"entities": [(18, 66, 'ADDRESS')]}),

    ("New card 5306769570464196 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Card 379474597402221 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Recovery email set to gw9xd22lnwwigeu@gmail.com.",
     {"entities": [(22, 47, 'EMAIL')]}),

    ("Transaction on card 6084256323174465 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Customer lives at Khasra No 854, Kasna, near Pepsi Agency, Kasna Village, Greater Noida.",
     {"entities": [(18, 87, 'ADDRESS')]}),

    ("Billing address: Roadways, Husainabad, Jaunpur, Uttar Pradesh 222002.",
     {"entities": [(17, 68, 'ADDRESS')]}),

    ("Send OTP to ptz626lgbzfg_1@gmail.com immediately.",
     {"entities": [(12, 36, 'EMAIL')]}),

    ("Rekha Iyer at F828+3VG, Shamli, Uttar Pradesh 247776, email u8bbpz9ldsrjto@gmail.com.",
     {"entities": [(0, 10, 'PERSON'), (14, 52, 'ADDRESS'), (60, 84, 'EMAIL')]}),

    ("Please contact ht2g0rczbze55lfhj@gmail.com for queries.",
     {"entities": [(15, 42, 'EMAIL')]}),

    ("Send OTP to r9wjhuz171yp7@gmail.com immediately.",
     {"entities": [(12, 35, 'EMAIL')]}),

    ("Verify card 6006170442058294 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Invoice to be sent at Garh Rd, near K.L. International School, Sector 8, Jagrati Vihar, Meerut.",
     {"entities": [(22, 94, 'ADDRESS')]}),

    ("Statement sent to p_24hia0frj1@gmail.com successfully.",
     {"entities": [(18, 40, 'EMAIL')]}),

    ("Card 4905202917099485 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Please contact o9pd8g4i9qxr5rsbksl@gmail.com for queries.",
     {"entities": [(15, 44, 'EMAIL')]}),

    ("Ananya Krishnamurthy used card 6568292123726959 at 9JJ3+PCM, near DELHI PUBLIC SCHOOL, Awas Vikas Colony, Farrukhabad.",
     {"entities": [(0, 20, 'PERSON'), (31, 47, 'CREDIT_CARD'), (51, 117, 'ADDRESS')]}),

    ("Office is at Plot No 284, Sector 6, Pocket 5, Jasola Vihar, New Delhi, Delhi 110025.",
     {"entities": [(13, 83, 'ADDRESS')]}),

    ("Transaction on card 6052030952178455 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Charge card number 5277105695182379 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Card 6087905563836992 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Recovery email set to r1tfwbj@gmail.com.",
     {"entities": [(22, 39, 'EMAIL')]}),

    ("Send report to gmzt28bz2k0wgyp1fern@gmail.com.",
     {"entities": [(15, 45, 'EMAIL')]}),

    ("Verify card 6513882696856680 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Account linked to dg80i1l1ol5gtf@gmail.com.",
     {"entities": [(18, 42, 'EMAIL')]}),

    ("Registered address: Kartalpur, Bypass, Azamatpur Kodur, Sarai Mandraj, Azamgarh.",
     {"entities": [(20, 79, 'ADDRESS')]}),

    ("Charge card number 5583159064308530 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Notification sent to a59w80.qo5bs8@gmail.com.",
     {"entities": [(21, 44, 'EMAIL')]}),

    ("Geeta Rani at FQVW+H39, Chakia, Saket Nagar, Deoria, Uttar Pradesh 274001, email xyj7r5zuf37p@gmail.com.",
     {"entities": [(0, 10, 'PERSON'), (14, 73, 'ADDRESS'), (81, 103, 'EMAIL')]}),

    ("Transaction on card 4884243879388735 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("OTP sent to bwg8g@gmail.com.",
     {"entities": [(12, 27, 'EMAIL')]}),

    ("Email ykn.yws9v5zcl@gmail.com not verified.",
     {"entities": [(6, 29, 'EMAIL')]}),

    ("Registered address: Maal Godam Road, 19A, New Mandi, Muzaffarnagar, Uttar Pradesh 251001.",
     {"entities": [(20, 88, 'ADDRESS')]}),

    ("Office is at Kannauj, NH-91, Grand Trunk Road, Kannauj Mainpuri Road, Fatehpur.",
     {"entities": [(13, 78, 'ADDRESS')]}),

    ("Card 5299303792867642 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Payment failed for card 6548814351061177.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Bill sent to mh8ew3bba.bco6i@gmail.com for card 6032080720689578.",
     {"entities": [(13, 38, 'EMAIL'), (48, 64, 'CREDIT_CARD')]}),

    ("Verify card 6502930389716641 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("User registered with elf2hqvvye2@gmail.com.",
     {"entities": [(21, 42, 'EMAIL')]}),

    ("Card 6583235181006609 linked to cqbrug@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 48, 'EMAIL')]}),

    ("Statement sent to vs9vl1p3d@gmail.com successfully.",
     {"entities": [(18, 37, 'EMAIL')]}),

    ("Transaction on card 5377892418515732 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Sanjay Gupta at Q3H3+225, Sugar Mill Rd, Khalilabad, Banjaria Dehat, Uttar Pradesh 272175, email wdydkii2cdpea7de@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 89, 'ADDRESS'), (97, 123, 'EMAIL')]}),

    ("Send statement to v5xidw9r_nqcw53oux@gmail.com for Dinesh Rao.",
     {"entities": [(18, 46, 'EMAIL'), (51, 61, 'PERSON')]}),

    ("Send report to w6cs4gddc8_00ey7a@gmail.com.",
     {"entities": [(15, 42, 'EMAIL')]}),

    ("Property located at W6H6+CW4 JEBRA Park, Shivaji Puram, Siddarth Nagar, Palhari.",
     {"entities": [(20, 79, 'ADDRESS')]}),

    ("Send statement to z34lw@gmail.com for Sanjay Gupta.",
     {"entities": [(18, 33, 'EMAIL'), (38, 50, 'PERSON')]}),

    ("Email l30qo6pm2u.97zl5hwe@gmail.com not verified.",
     {"entities": [(6, 35, 'EMAIL')]}),

    ("Account linked to wmr6dt8h@gmail.com.",
     {"entities": [(18, 36, 'EMAIL')]}),

    ("Customer lives at Khan Chandpur, Rania, Uttar Pradesh 209304.",
     {"entities": [(18, 60, 'ADDRESS')]}),

    ("Send statement to o3_br9bv1kii5@gmail.com for Rahul Sharma.",
     {"entities": [(18, 41, 'EMAIL'), (46, 58, 'PERSON')]}),

    ("Notification sent to j9rzlnz6h3s9g@gmail.com.",
     {"entities": [(21, 44, 'EMAIL')]}),

    ("Property located at A-36, 2nd St, BLOCK SECTOR, Zeta I, Greater Noida, Uttar Pradesh 201306.",
     {"entities": [(20, 91, 'ADDRESS')]}),

    ("Email s13pnfczba_zjf@gmail.com not verified.",
     {"entities": [(6, 30, 'EMAIL')]}),

    ("Customer lives at 63Q2+PQ3, Avabagh Colony, Judges Colony, Mainpuri, Uttar Pradesh 205001.",
     {"entities": [(18, 89, 'ADDRESS')]}),

    ("Invoice to be sent at V3R3+JV8, Pratibha Colony, Nagla Masani, Aligarh, Uttar Pradesh 202001.",
     {"entities": [(22, 92, 'ADDRESS')]}),

    ("Send OTP to nuz2mrgqt8yomsfac@gmail.com immediately.",
     {"entities": [(12, 39, 'EMAIL')]}),

    ("Card 5587343207548173 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Branch office at Near Globus IT Park, Plot No 9, Knowledge Park III, Near Globus IT Park.",
     {"entities": [(17, 88, 'ADDRESS')]}),

    ("Ananya Krishnamurthy used card 4201732710281779 at 9, Park End, Vikas Marg, Delhi Park End Panjatani Co-op Housing Building.",
     {"entities": [(0, 20, 'PERSON'), (31, 47, 'CREDIT_CARD'), (51, 123, 'ADDRESS')]}),

    ("Please ship to JCQG+CGQ, Unnamed Road Bhim Nagar, Nai Basti, near kamla hall, Vijay Nagar.",
     {"entities": [(15, 89, 'ADDRESS')]}),

    ("Account linked to l0pdchpujz30ja@gmail.com.",
     {"entities": [(18, 42, 'EMAIL')]}),

    ("Charge card number 6504059338987377 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Payment failed for card 4090774105178886.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Branch office at C8R6+RXW, Road, near Bank of BadodaNirala nagar, U Block, Juhi Kalan, Juhi.",
     {"entities": [(17, 91, 'ADDRESS')]}),

    ("Account linked to ac.2euq5v_wb@gmail.com.",
     {"entities": [(18, 40, 'EMAIL')]}),

    ("Please ship to 5R44+8Q6, Amethi, Uttar Pradesh 227405.",
     {"entities": [(15, 53, 'ADDRESS')]}),

    ("Rohit Mehta at 11/43, Mohsin -E- Azam Colony, Shaadi Nagar, Rampur, Uttar Pradesh 244901, email z2ucj.dp@gmail.com.",
     {"entities": [(0, 11, 'PERSON'), (15, 88, 'ADDRESS'), (96, 114, 'EMAIL')]}),

    ("Office is at PQH8+F5W, Delhi road, near SSV PG College, Arjun Nagar, Hapur.",
     {"entities": [(13, 74, 'ADDRESS')]}),

    ("Recovery email set to yrm6ho6ch8@gmail.com.",
     {"entities": [(22, 42, 'EMAIL')]}),

    ("OTP sent to naikzyz.886xj6@gmail.com.",
     {"entities": [(12, 36, 'EMAIL')]}),

    ("Send report to wo22x5r2bootdj4dkok@gmail.com.",
     {"entities": [(15, 44, 'EMAIL')]}),

    ("Invoice to be sent at JRXC+4GM, Officer's Colony, Pilibhit, Uttar Pradesh 262001.",
     {"entities": [(22, 80, 'ADDRESS')]}),

    ("Payment failed for card 374711420809679.",
     {"entities": [(24, 39, 'CREDIT_CARD')]}),

    ("Kiran Bedi card 4409897913679519 blocked.",
     {"entities": [(0, 10, 'PERSON'), (16, 32, 'CREDIT_CARD')]}),

    ("Card 6026922740789024 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Send documents to GRGH+MVM, Sithmara, Uttar Pradesh 209302.",
     {"entities": [(18, 58, 'ADDRESS')]}),

    ("Card 5557316537440754 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Send statement to jyoybzgb@gmail.com for Sanjay Gupta.",
     {"entities": [(18, 36, 'EMAIL'), (41, 53, 'PERSON')]}),

    ("Charge card number 4927137227837860 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Billing address: Deegha, Uttar Pradesh 272175.",
     {"entities": [(17, 45, 'ADDRESS')]}),

    ("Kiran Bedi card 6529926300238329 blocked.",
     {"entities": [(0, 10, 'PERSON'), (16, 32, 'CREDIT_CARD')]}),

    ("Transaction on card 6053886132904810 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Deepika Nair at VFJ9+QMM, Dasipur, Amroha, Uttar Pradesh 244221, email m3xfu@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 63, 'ADDRESS'), (71, 86, 'EMAIL')]}),

    ("Please contact xk5ws@gmail.com for queries.",
     {"entities": [(15, 30, 'EMAIL')]}),

    ("OTP sent to pdnprtjg_jix@gmail.com.",
     {"entities": [(12, 34, 'EMAIL')]}),

    ("Office is at Q2XC+8R6, Mohsin -E- Azam Colony, Civil Lines, Rampur, Uttar Pradesh 244901.",
     {"entities": [(13, 88, 'ADDRESS')]}),

    ("Card 6510921837277104 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Send documents to 3W27+HF7, Mohalla Kazi Tola, Paraspur, Kannauj, Uttar Pradesh 209727.",
     {"entities": [(18, 86, 'ADDRESS')]}),

    ("Card 378551179624823 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Billing address: Main Road, C-Block, Dilshad Garden, Delhi, 110095.",
     {"entities": [(17, 66, 'ADDRESS')]}),

    ("Ananya Krishnamurthy at 5/183-B, Vipul Khand 5, Vipul Khand, Gomti Nagar, Lucknow, email bzjku14t5i@gmail.com.",
     {"entities": [(0, 20, 'PERSON'), (24, 81, 'ADDRESS'), (89, 109, 'EMAIL')]}),

    ("Notification sent to trbv9yah15@gmail.com.",
     {"entities": [(21, 41, 'EMAIL')]}),

    ("Account linked to okmpkdele3xck@gmail.com.",
     {"entities": [(18, 41, 'EMAIL')]}),

    ("Card 4733011454200122 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Neha Joshi at C5CP+5JQ, Balrampur, Uttar Pradesh 271201, email lytkru7e2kp.zgj@gmail.com.",
     {"entities": [(0, 10, 'PERSON'), (14, 55, 'ADDRESS'), (63, 88, 'EMAIL')]}),

    ("Email lf184396t@gmail.com not verified.",
     {"entities": [(6, 25, 'EMAIL')]}),

    ("OTP sent to nhqa3kujqb8@gmail.com.",
     {"entities": [(12, 33, 'EMAIL')]}),

    ("Card 4156730671361711 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Card 6536259329663637 linked to mi5an71s2oj@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 53, 'EMAIL')]}),

    ("New card 343106239876032 issued to customer.",
     {"entities": [(9, 24, 'CREDIT_CARD')]}),

    ("Notification sent to ngdws@gmail.com.",
     {"entities": [(21, 36, 'EMAIL')]}),

    ("Charge card number 370334807516152 for INR 2000.",
     {"entities": [(19, 34, 'CREDIT_CARD')]}),

    ("Customer Shruti Desai lives at Q2JV+MV3, Khalilabad, Patkhauli, Uttar Pradesh 272175. Contact: hecq.6pftimt0@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 84, 'ADDRESS'), (95, 118, 'EMAIL')]}),

    ("Card 6530935052524878 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Rohit Mehta card 6544048970932827 blocked.",
     {"entities": [(0, 11, 'PERSON'), (17, 33, 'CREDIT_CARD')]}),

    ("Billing address: Pocket 45, 45/9, Rajapur, Razapur, Sector 9, Rohini, New Delhi, Delhi.",
     {"entities": [(17, 86, 'ADDRESS')]}),

    ("Payment failed for card 4071796072579790.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Send documents to Shiv Puri, State Highway 12, Bhopa Rd, Muzaffarnagar, Uttar Pradesh 251001.",
     {"entities": [(18, 92, 'ADDRESS')]}),

    ("Office is at Sahar Khas Dakhini, Shahjahanpur, Uttar Pradesh 242001.",
     {"entities": [(13, 67, 'ADDRESS')]}),

    ("New card 6556496133288267 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Payment failed for card 4793166130456129.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Customer Geeta Rani lives at Gopal Nagar, Fatehpur, Uttar Pradesh 212601. Contact: wfz3fatin@gmail.com.",
     {"entities": [(9, 19, 'PERSON'), (29, 72, 'ADDRESS'), (83, 102, 'EMAIL')]}),

    ("Delivery address is Maa Sharda Nagar, Near, Lohramau temple Road, opp. Tata Motors, Mahuariya.",
     {"entities": [(20, 93, 'ADDRESS')]}),

    ("Send documents to 9HW2+GX5, Street No. 2, Bhadohi Nagar Palika, Raya, Uttar Pradesh 221401.",
     {"entities": [(18, 90, 'ADDRESS')]}),

    ("Email ycyzpd2qogxkn0ry944i@gmail.com not verified.",
     {"entities": [(6, 36, 'EMAIL')]}),

    ("Office is at P4HW+9R6, Khiridand, Sant Kabir Nagar, Uttar Pradesh 273212.",
     {"entities": [(13, 72, 'ADDRESS')]}),

    ("Office is at G 336, Block I, G-Block, Govindpuram, Ghaziabad, Uttar Pradesh 201013.",
     {"entities": [(13, 82, 'ADDRESS')]}),

    ("Disputed transaction on card 5503092681382237.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Disputed transaction on card 5123809620782755.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Send OTP to eqqk_k4@gmail.com immediately.",
     {"entities": [(12, 29, 'EMAIL')]}),

    ("Bill sent to tuunk0rgh3w.wpnnjv@gmail.com for card 4548235876689014.",
     {"entities": [(13, 41, 'EMAIL'), (51, 67, 'CREDIT_CARD')]}),

    ("Please ship to Karnal - Shamli Rd, near BSM School, Shamli, Mundetkalan.",
     {"entities": [(15, 71, 'ADDRESS')]}),

    ("Verify card 4403358680900187 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Transaction on card 6058438795716046 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Billing address: Sai mandir choona chakki, Pakka Talab Rd, Purbia Tola, Etawah.",
     {"entities": [(17, 78, 'ADDRESS')]}),

    ("Invoice to be sent at 17, Dwarika Puri, Muzaffarnagar, Uttar Pradesh 251001.",
     {"entities": [(22, 75, 'ADDRESS')]}),

    ("OTP sent to fc8zzlcj2_fljpflw2h@gmail.com.",
     {"entities": [(12, 41, 'EMAIL')]}),

    ("Block card 4587739022479556 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Email mx0kc05dpony253qtg@gmail.com not verified.",
     {"entities": [(6, 34, 'EMAIL')]}),

    ("Email ff8rsojym2gddl@gmail.com not verified.",
     {"entities": [(6, 30, 'EMAIL')]}),

    ("Please contact fzltgnuo140cge@gmail.com for queries.",
     {"entities": [(15, 39, 'EMAIL')]}),

    ("Customer lives at 16/12, Neil Rd, Civil Lines, Kanpur, Uttar Pradesh 208001.",
     {"entities": [(18, 75, 'ADDRESS')]}),

    ("Email ck9p4dsxstk_fsm@gmail.com not verified.",
     {"entities": [(6, 31, 'EMAIL')]}),

    ("Suresh Patel at near B.R.D. Inter College, Tube Well Colony, New Colony, Deoria, email sa4.uj373qxzff@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 79, 'ADDRESS'), (87, 111, 'EMAIL')]}),

    ("Please ship to Near, Lalitpur Railway Station Rd, Civil Lines, Lalitpur.",
     {"entities": [(15, 71, 'ADDRESS')]}),

    ("Charge card number 4989266360394069 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("OTP sent to s.1e12aogosyrod7@gmail.com.",
     {"entities": [(12, 38, 'EMAIL')]}),

    ("Invoice to be sent at J75Q+V35, Chatan Jain Marg, Mayur Vihar, New Delhi, Delhi, 110091.",
     {"entities": [(22, 87, 'ADDRESS')]}),

    ("User registered with spx63c2s3av@gmail.com.",
     {"entities": [(21, 42, 'EMAIL')]}),

    ("Customer Shruti Desai lives at PMXM+9R8, Olandganj, Jaunpur, Uttar Pradesh 222002. Contact: b9fh074b@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 81, 'ADDRESS'), (92, 110, 'EMAIL')]}),

    ("Customer Rekha Iyer lives at Saharanpur - Delhi Rd, Jalalabad, Thanabhawan, Uttar Pradesh 247772. Contact: dqilt@gmail.com.",
     {"entities": [(9, 19, 'PERSON'), (29, 96, 'ADDRESS'), (107, 122, 'EMAIL')]}),

    ("Disputed transaction on card 4981397562986752.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Statement sent to v59kzz@gmail.com successfully.",
     {"entities": [(18, 34, 'EMAIL')]}),

    ("Customer Nisha Agarwal lives at M69J+C2G, Inter State Bus Terminal, Kashmere Gate, Delhi, 110006. Contact: px_co35culzd@gmail.com.",
     {"entities": [(9, 22, 'PERSON'), (32, 96, 'ADDRESS'), (107, 129, 'EMAIL')]}),

    ("Billing address: T-8, Partappura, Shahdara, Delhi, 110032.",
     {"entities": [(17, 57, 'ADDRESS')]}),

    ("Please contact bnld58njpi41mpodbpl@gmail.com for queries.",
     {"entities": [(15, 44, 'EMAIL')]}),

    ("Account linked to uihsbzlr1@gmail.com.",
     {"entities": [(18, 37, 'EMAIL')]}),

    ("Card 6090274589171017 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Customer Priya Singh lives at E-1036, Budh Nagar, Inder Puri, New Delhi, Delhi 110028. Contact: eu8ze1mvbrf_0@gmail.com.",
     {"entities": [(9, 20, 'PERSON'), (30, 85, 'ADDRESS'), (96, 119, 'EMAIL')]}),

    ("Please ship to Q3V9+3M5, Bahuara, Bahura, Uttar Pradesh 231216.",
     {"entities": [(15, 62, 'ADDRESS')]}),

    ("Registered address: 7A/45, Channa Market, Channa Market, Block 7A, WEA, Karol Bagh, Delhi.",
     {"entities": [(20, 89, 'ADDRESS')]}),

    ("Send documents to Bangali Ghat, Mathura, Uttar Pradesh 281001.",
     {"entities": [(18, 61, 'ADDRESS')]}),

    ("Dinesh Rao at Chak Bisauli, Fatehpur, Uttar Pradesh 212601, email n_quugnlg1puzdo5r@gmail.com.",
     {"entities": [(0, 10, 'PERSON'), (14, 58, 'ADDRESS'), (66, 93, 'EMAIL')]}),

    ("Disputed transaction on card 6584480104323423.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Bill sent to pcbd7ygywcve@gmail.com for card 370887225193700.",
     {"entities": [(13, 35, 'EMAIL'), (45, 60, 'CREDIT_CARD')]}),

    ("Billing address: 48VP+VW5, Mohalla Joshiyana, Jalaun, Uttar Pradesh 285123.",
     {"entities": [(17, 74, 'ADDRESS')]}),

    ("Billing address: Main Banthala, Chirodi Rd, Loni Dehat, Ghaziabad, Uttar Pradesh 201102.",
     {"entities": [(17, 87, 'ADDRESS')]}),

    ("Block card 6521525652626120 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Office is at Muzaffarpur, Uttar Pradesh 232111.",
     {"entities": [(13, 46, 'ADDRESS')]}),

    ("Card 348268461412861 linked to g5btrt@gmail.com.",
     {"entities": [(5, 20, 'CREDIT_CARD'), (31, 47, 'EMAIL')]}),

    ("Registered address: 36/D, Pracheen Sai Dham Mandir, Guru Ravi Das Marg.",
     {"entities": [(20, 70, 'ADDRESS')]}),

    ("Invoice to be sent at 5H35+6F6, Azad Nagar, Maupakar, Maharajganj, Uttar Pradesh 273303.",
     {"entities": [(22, 87, 'ADDRESS')]}),

    ("Branch office at M5CP+F42, Gulabi Bagh, New Delhi, Delhi, 110007.",
     {"entities": [(17, 64, 'ADDRESS')]}),

    ("Registered address: Shop No. 14, Kamla Nehru Institute Of Technology, Sultanpur, Ratan Pur.",
     {"entities": [(20, 90, 'ADDRESS')]}),

    ("Notification sent to wdqy5@gmail.com.",
     {"entities": [(21, 36, 'EMAIL')]}),

    ("Disputed transaction on card 5424010196503866.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Customer Ananya Krishnamurthy lives at 5R35+WR4, Sarvan Pur, Amethi, Uttar Pradesh 227405. Contact: b8bnwrx5rtssh2u0f@gmail.com.",
     {"entities": [(9, 29, 'PERSON'), (39, 89, 'ADDRESS'), (100, 127, 'EMAIL')]}),

    ("Branch office at XG9P+9M8, NH73, Jatav Nagar, Purani Mandi, Saharanpur, Uttar Pradesh 247001.",
     {"entities": [(17, 92, 'ADDRESS')]}),

    ("Send report to u6xcxow0@gmail.com.",
     {"entities": [(15, 33, 'EMAIL')]}),

    ("Branch office at RAILWAY ROAD HAPUR(50581, Uttar Pradesh 245101.",
     {"entities": [(17, 63, 'ADDRESS')]}),

    ("Invoice to be sent at 157, Delhi road, near Hari Mandir Road, Pradyuman Nagar, Avas Vikas Colony.",
     {"entities": [(22, 96, 'ADDRESS')]}),

    ("Customer Rohit Mehta lives at IBP Chauraha, downward side Bank of Baroda, near petrol pump. Contact: fkjw.x1odm6uj@gmail.com.",
     {"entities": [(9, 20, 'PERSON'), (30, 90, 'ADDRESS'), (101, 124, 'EMAIL')]}),

    ("Send documents to Bhoor Chauraha, Bulandshahr, NH-91, Grand Trank Road, Bulandshahar.",
     {"entities": [(18, 84, 'ADDRESS')]}),

    ("Card 6090260135790313 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Send OTP to gfkf8foa.pn@gmail.com immediately.",
     {"entities": [(12, 33, 'EMAIL')]}),

    ("Billing address: M8C4+WPX, Jhilmil Colony, Pratap Khand, Jhilmil Colony, New Delhi.",
     {"entities": [(17, 82, 'ADDRESS')]}),

    ("Recovery email set to midgosjgq651@gmail.com.",
     {"entities": [(22, 44, 'EMAIL')]}),

    ("Send report to zo48gn@gmail.com.",
     {"entities": [(15, 31, 'EMAIL')]}),

    ("Card 5381140959409670 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Card 5209674209821667 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Manoj Tiwari used card 4184547829414639 at Bajpai Colony, Maharaj Nagar, Lakhimpur, Uttar Pradesh 262701.",
     {"entities": [(0, 12, 'PERSON'), (23, 39, 'CREDIT_CARD'), (43, 104, 'ADDRESS')]}),

    ("Email ykvzskytdrkoy@gmail.com not verified.",
     {"entities": [(6, 29, 'EMAIL')]}),

    ("Office is at ward no- 2, Maa kali mandir, Ramkola, Uttar Pradesh 274305.",
     {"entities": [(13, 71, 'ADDRESS')]}),

    ("Billing address: Shahzadi sarai, opposite RTO Office, Sambhal, Uttar Pradesh 244302.",
     {"entities": [(17, 83, 'ADDRESS')]}),

    ("Card 373908563508334 linked to ii74.5_uj@gmail.com.",
     {"entities": [(5, 20, 'CREDIT_CARD'), (31, 50, 'EMAIL')]}),

    ("Card 377687685524985 linked to t29_dffr@gmail.com.",
     {"entities": [(5, 20, 'CREDIT_CARD'), (31, 49, 'EMAIL')]}),

    ("Send documents to Building no 30, near Deer Park, Hauz Khas Village, Deer Park, Hauz Khas.",
     {"entities": [(18, 89, 'ADDRESS')]}),

    ("Disputed transaction on card 4082491476359421.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Statement sent to tvuf6diu@gmail.com successfully.",
     {"entities": [(18, 36, 'EMAIL')]}),

    ("Property located at PVRQ+CW2, Buddha Marg, Kushinagar, Sonbarsa, Uttar Pradesh 274403.",
     {"entities": [(20, 85, 'ADDRESS')]}),

    ("Send documents to Paṭhan tola, Mehadawal Khalilabad Maghar Marg, Khalilabad.",
     {"entities": [(18, 75, 'ADDRESS')]}),

    ("Charge card number 4895031619582508 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Amit Kumar card 375028277861034 blocked.",
     {"entities": [(0, 10, 'PERSON'), (16, 31, 'CREDIT_CARD')]}),

    ("Send OTP to prdj4@gmail.com immediately.",
     {"entities": [(12, 27, 'EMAIL')]}),

    ("Email ukv7yhn_i@gmail.com not verified.",
     {"entities": [(6, 25, 'EMAIL')]}),

    ("Card 346158107255057 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Suresh Patel card 346939997742371 blocked.",
     {"entities": [(0, 12, 'PERSON'), (18, 33, 'CREDIT_CARD')]}),

    ("New card 6035435443458730 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Please ship to Block Office, Nath Nagar, Barauli, Uttar Pradesh 272176.",
     {"entities": [(15, 70, 'ADDRESS')]}),

    ("Statement sent to x9prwgui4@gmail.com successfully.",
     {"entities": [(18, 37, 'EMAIL')]}),

    ("Send report to zn3f.k4_g@gmail.com.",
     {"entities": [(15, 34, 'EMAIL')]}),

    ("Charge card number 4048074278223810 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Delivery address is 8 Madhuvan Enclave NH-2 Between Jain Furniture and Sharma Hospital.",
     {"entities": [(20, 86, 'ADDRESS')]}),

    ("Registered address: South Gautam Nagar, Gautam Nagar, Fatehpur, Uttar Pradesh 212601.",
     {"entities": [(20, 84, 'ADDRESS')]}),

    ("Card 5519436974103434 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Property located at Health City Hospital Road, NH-A/B, Vijay Khand Marg, Vijay Khand 2.",
     {"entities": [(20, 86, 'ADDRESS')]}),

    ("Card 5238335180534996 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Branch office at P BIJHAULI, BIJHOULI, Pachperwa, Uttar Pradesh 262701.",
     {"entities": [(17, 70, 'ADDRESS')]}),

    ("Payment failed for card 4500725377745462.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Send documents to 3rd Floor, 143, Street Number 12, Jamia Nagar, Jogabai Extension.",
     {"entities": [(18, 82, 'ADDRESS')]}),

    ("Customer lives at A - 4, FNG VIHAR, 1, Faridabad - Noida - Ghaziabad Expy, Sector 121, Noida.",
     {"entities": [(18, 92, 'ADDRESS')]}),

    ("Delivery address is Loha Mandi Road, Bisat Khana, Agrawal Mohalla, Mainpuri.",
     {"entities": [(20, 75, 'ADDRESS')]}),

    ("Please contact p08wm7omuyirhwf@gmail.com for queries.",
     {"entities": [(15, 40, 'EMAIL')]}),

    ("Customer Neha Joshi lives at Railway Station, Karari, Jhansi, Uttar Pradesh 284003. Contact: ldx6at@gmail.com.",
     {"entities": [(9, 19, 'PERSON'), (29, 82, 'ADDRESS'), (93, 109, 'EMAIL')]}),

    ("New card 370716372583847 issued to customer.",
     {"entities": [(9, 24, 'CREDIT_CARD')]}),

    ("Please ship to 53/30, 53/30, Geeta Rd, Geeta Puram, Ab Nagar, Unnao, Uttar Pradesh 209801.",
     {"entities": [(15, 89, 'ADDRESS')]}),

    ("Card 4093626371059738 linked to bq_3p34r9pohnmwt@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 58, 'EMAIL')]}),

    ("Recovery email set to beubcrflvo7@gmail.com.",
     {"entities": [(22, 43, 'EMAIL')]}),

    ("Send OTP to cm4uq_vw@gmail.com immediately.",
     {"entities": [(12, 30, 'EMAIL')]}),

    ("New card 6056482912076877 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Charge card number 6564954565391212 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Send documents to J8XQ+CF2, Gaur Ganga Apartment, Yashoda Marg, near Metro Station, Sector 4.",
     {"entities": [(18, 92, 'ADDRESS')]}),

    ("User registered with t0fy55u_ns2du1hkopx@gmail.com.",
     {"entities": [(21, 50, 'EMAIL')]}),

    ("Tarun Khanna at Malgodam Road, Ghazipur, Uttar Pradesh 233001, email tjd5dtfrcp@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 61, 'ADDRESS'), (69, 89, 'EMAIL')]}),

    ("OTP sent to w9fnyab33@gmail.com.",
     {"entities": [(12, 31, 'EMAIL')]}),

    ("Bill sent to y_4xmkll.a@gmail.com for card 6517017567886178.",
     {"entities": [(13, 33, 'EMAIL'), (43, 59, 'CREDIT_CARD')]}),

    ("Notification sent to c7i.kq9y68pzw@gmail.com.",
     {"entities": [(21, 44, 'EMAIL')]}),

    ("Invoice to be sent at HM47+3M8, Shikohabad Rd, Etah, Uttar Pradesh 207001.",
     {"entities": [(22, 73, 'ADDRESS')]}),

    ("Delivery address is Gaur Yamuna City, Yamuna Expy, Greater Noida, Uttar Pradesh 203201.",
     {"entities": [(20, 86, 'ADDRESS')]}),

    ("Invoice to be sent at 2nd Floor, near Doordarshan Kendra, Indian Post, Varanasi.",
     {"entities": [(22, 79, 'ADDRESS')]}),

    ("Payment failed for card 373240860735721.",
     {"entities": [(24, 39, 'CREDIT_CARD')]}),

    ("Disputed transaction on card 4510314136541745.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Send report to tbw.m65hdi.muu0@gmail.com.",
     {"entities": [(15, 40, 'EMAIL')]}),

    ("Invoice to be sent at R243+5JH, H.N. Nagar, Etawah, Uttar Pradesh 206002.",
     {"entities": [(22, 72, 'ADDRESS')]}),

    ("Meena Patel at 41/142, A/1 VIP Road-Taj Mahal Road, Fatehabad Rd, Agra, email lbjdjgzaegd5alipz@gmail.com.",
     {"entities": [(0, 11, 'PERSON'), (15, 70, 'ADDRESS'), (78, 105, 'EMAIL')]}),

    ("Branch office at Bhartiya Vidhyalya Ke Pass, Defence Institute, Dibiyapur Rd, Govind Nagar.",
     {"entities": [(17, 90, 'ADDRESS')]}),

    ("Verify card 4576064300287915 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Send statement to gmc3s8n@gmail.com for Deepika Nair.",
     {"entities": [(18, 35, 'EMAIL'), (40, 52, 'PERSON')]}),

    ("Charge card number 5433732419197450 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Statement sent to g7178lkq65pm2dal5mow@gmail.com successfully.",
     {"entities": [(18, 48, 'EMAIL')]}),

    ("Billing address: Faizabad - Allahabad Rd, Ajeet Nagar, MAIN ROAD, Pratapgarh.",
     {"entities": [(17, 76, 'ADDRESS')]}),

    ("Send report to m_0bu8d9jmdbz3.l@gmail.com.",
     {"entities": [(15, 41, 'EMAIL')]}),

    ("Card 349788898226483 linked to this account.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Delivery address is Chhittupur, Shivpurwa, Varanasi, Uttar Pradesh 221010.",
     {"entities": [(20, 73, 'ADDRESS')]}),

    ("Transaction on card 5165507405929481 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Send OTP to v3wu2l3dadi@gmail.com immediately.",
     {"entities": [(12, 33, 'EMAIL')]}),

    ("Invoice to be sent at XQ4W+PC5, Naurangabad, Banwaripur, Uttar Pradesh 262701.",
     {"entities": [(22, 77, 'ADDRESS')]}),

    ("Card 6045449314076320 linked to fqfo_68y28pz5r1v@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 58, 'EMAIL')]}),

    ("Notification sent to qwo46tho_jj2@gmail.com.",
     {"entities": [(21, 43, 'EMAIL')]}),

    ("Dinesh Rao used card 4041973621215544 at A-56, Oldanpur, Block B, Jyoti Colony, Shahdara, Delhi, 110032.",
     {"entities": [(0, 10, 'PERSON'), (21, 37, 'CREDIT_CARD'), (41, 103, 'ADDRESS')]}),

    ("Card 5236400705594961 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Recovery email set to y9h6i3w377cd9hg679g@gmail.com.",
     {"entities": [(22, 51, 'EMAIL')]}),

    ("Customer Manoj Tiwari lives at S-2/635, Hamrautia, Varanasi, Uttar Pradesh 221002. Contact: qb8ioztb@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 81, 'ADDRESS'), (92, 110, 'EMAIL')]}),

    ("Billing address: Senapati Bapat Rd, next to JW MARRIOTT HOTEL, Laxmi Society, Model Colony.",
     {"entities": [(17, 90, 'ADDRESS')]}),

    ("Charge card number 5409835799212599 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Transaction on card 4403682652505534 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Transaction on card 4331559879072672 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Send report to n4pqm9wrja@gmail.com.",
     {"entities": [(15, 35, 'EMAIL')]}),

    ("Card 377987435584979 was used at ATM.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Send documents to WX8H+3V2, Ashtbhuja Nagar, Pratapgarh, Bela Pratapgarh, Sagra.",
     {"entities": [(18, 79, 'ADDRESS')]}),

    ("Payment failed for card 5277040179594475.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Bill sent to tui1_vmp1rykbynve5n@gmail.com for card 6506849150416602.",
     {"entities": [(13, 42, 'EMAIL'), (52, 68, 'CREDIT_CARD')]}),

    ("Card 5124854100967608 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Property located at JRC3+5PG, Vipul Medical store, Rama College Road.",
     {"entities": [(20, 68, 'ADDRESS')]}),

    ("Card 4756658084709005 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Please contact ykrsxlc2y._ewj8nff.3@gmail.com for queries.",
     {"entities": [(15, 45, 'EMAIL')]}),

    ("Please contact fhkdiid8e6f.gts@gmail.com for queries.",
     {"entities": [(15, 40, 'EMAIL')]}),

    ("Please ship to 48WP+W7C, Way To Kalindri Talkies, Haripura, Jalaun, Uttar Pradesh 285123.",
     {"entities": [(15, 88, 'ADDRESS')]}),

    ("Billing address: NOOR MASJID, Ajay Nagar Colony, Netaji Subas Chandra Bos Nagar Colony.",
     {"entities": [(17, 86, 'ADDRESS')]}),

    ("Recovery email set to wki9du69m32t@gmail.com.",
     {"entities": [(22, 44, 'EMAIL')]}),

    ("Recovery email set to whlcbevh_5@gmail.com.",
     {"entities": [(22, 42, 'EMAIL')]}),

    ("Customer lives at 52RG+G34, Belanganj, Civil Lines, Agra, Uttar Pradesh 282003.",
     {"entities": [(18, 78, 'ADDRESS')]}),

    ("Please contact go_35ca77@gmail.com for queries.",
     {"entities": [(15, 34, 'EMAIL')]}),

    ("Invoice to be sent at JX5M+X4X, Najafgarh Thana Rd, Najafgarh, Delhi, 110043.",
     {"entities": [(22, 76, 'ADDRESS')]}),

    ("Card 348756822124224 was used at ATM.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Customer Sunita Verma lives at J83F+Q2W, Dallupura Rd, Vasundhara Enclave, New Delhi, Delhi, 110096. Contact: pa.9go80@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 99, 'ADDRESS'), (110, 128, 'EMAIL')]}),

    ("Tarun Khanna used card 4217802334550891 at Malgodam Rd, NEAR STATION, Gautam Budha Colony, Malgodam Road, Ghazipur.",
     {"entities": [(0, 12, 'PERSON'), (23, 39, 'CREDIT_CARD'), (43, 114, 'ADDRESS')]}),

    ("Invoice to be sent at MLB MEDICAL COLLEGE Gate no. 1 and 2 ke samne.",
     {"entities": [(22, 67, 'ADDRESS')]}),

    ("Card 4660025175312621 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Office is at Chilla, Dda Market, ICICI Bank Ltd, F4 5, Csc Near Nav Jagruti Chs.",
     {"entities": [(13, 79, 'ADDRESS')]}),

    ("Email sv.ia65hle5sbo@gmail.com not verified.",
     {"entities": [(6, 30, 'EMAIL')]}),

    ("Billing address: Major Bhupinder Singh Nagar, Keshopur, Vikaspuri, Delhi, 110018.",
     {"entities": [(17, 80, 'ADDRESS')]}),

    ("Card 370016546743449 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Registered address: 7R7V+M5M, Mirtala, Uttar Pradesh 210427.",
     {"entities": [(20, 59, 'ADDRESS')]}),

    ("Statement sent to mv1tyxk4r_2iu_h.hc@gmail.com successfully.",
     {"entities": [(18, 46, 'EMAIL')]}),

    ("Disputed transaction on card 5301199462517186.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Office is at A-3,Ground floor, Eleven Orchid, Delhi Rd, Moradabad, 2440001.",
     {"entities": [(13, 74, 'ADDRESS')]}),

    ("Invoice to be sent at Dr. Mushtaq’s Mercy Health Clinic, Laddhawala, Muzaffarnagar.",
     {"entities": [(22, 82, 'ADDRESS')]}),

    ("OTP sent to vumljc9fl5@gmail.com.",
     {"entities": [(12, 32, 'EMAIL')]}),

    ("Delivery address is Railway Station Rd, Beharipur, Bareilly, Uttar Pradesh 243003.",
     {"entities": [(20, 81, 'ADDRESS')]}),

    ("Card 343525851681552 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Please contact lolasau2qeuoesg@gmail.com for queries.",
     {"entities": [(15, 40, 'EMAIL')]}),

    ("Delivery address is HHM5+7VP, Shivdham Colony, Pithapur, Fatehpur Sikandar, Ghazipur.",
     {"entities": [(20, 84, 'ADDRESS')]}),

    ("Payment failed for card 6080173975132680.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Customer lives at Udaan Library Bada, Parade Ground, near BSNL Tower, Balrampur.",
     {"entities": [(18, 79, 'ADDRESS')]}),

    ("Email qaajyr04@gmail.com not verified.",
     {"entities": [(6, 24, 'EMAIL')]}),

    ("Priya Singh card 4915597644117441 blocked.",
     {"entities": [(0, 11, 'PERSON'), (17, 33, 'CREDIT_CARD')]}),

    ("Recovery email set to z41fio3fevhvpwgh4id@gmail.com.",
     {"entities": [(22, 51, 'EMAIL')]}),

    ("Charge card number 375096428814369 for INR 2000.",
     {"entities": [(19, 34, 'CREDIT_CARD')]}),

    ("Invoice to be sent at 2/4, Awas Vikas Colony, Barabanki, Uttar Pradesh 225001.",
     {"entities": [(22, 77, 'ADDRESS')]}),

    ("User registered with avqk2vg1zr0to@gmail.com.",
     {"entities": [(21, 44, 'EMAIL')]}),

    ("Property located at 39-A, Rajghat Colony, Awas Vikas Colony, Ayodhya, Uttar Pradesh 224123.",
     {"entities": [(20, 90, 'ADDRESS')]}),

    ("Kiran Bedi used card 6001928261987737 at WQHX+R99, Civil Lines, Fatehpur, Uttar Pradesh 212601.",
     {"entities": [(0, 10, 'PERSON'), (21, 37, 'CREDIT_CARD'), (41, 94, 'ADDRESS')]}),

    ("Send report to novilpxkwugn@gmail.com.",
     {"entities": [(15, 37, 'EMAIL')]}),

    ("Account linked to q7curgpq6b80n5s3@gmail.com.",
     {"entities": [(18, 44, 'EMAIL')]}),

    ("Invoice to be sent at 2/14, near Bank of, Block 16, Subhash Nagar, New Delhi, Delhi, 110027.",
     {"entities": [(22, 91, 'ADDRESS')]}),

    ("User registered with ab4ybq9hyj3l_zftp5@gmail.com.",
     {"entities": [(21, 49, 'EMAIL')]}),

    ("Account linked to vbejav8a9an_3d@gmail.com.",
     {"entities": [(18, 42, 'EMAIL')]}),

    ("Statement sent to bdoqy4quou76n_3@gmail.com successfully.",
     {"entities": [(18, 43, 'EMAIL')]}),

    ("Nisha Agarwal at Sambhal, Uttar Pradesh 244302, email zuupky55m5u_tj@gmail.com.",
     {"entities": [(0, 13, 'PERSON'), (17, 46, 'ADDRESS'), (54, 78, 'EMAIL')]}),

    ("Payment failed for card 5175845956830914.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Please contact w9v7r@gmail.com for queries.",
     {"entities": [(15, 30, 'EMAIL')]}),

    ("Block card 4059086049554676 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Neha Joshi at HHJ4+6JM, Narotamsarai, Uttar Pradesh 244302, email r_vo32a7qfqapmw@gmail.com.",
     {"entities": [(0, 10, 'PERSON'), (14, 58, 'ADDRESS'), (66, 91, 'EMAIL')]}),

    ("Block card 5515497839218946 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Neha Joshi at 6W79+MF8, Traffic Chauraha karwi dikhau, Chitrakoot Dham, email vzxi2z_fbbn3co@gmail.com.",
     {"entities": [(0, 10, 'PERSON'), (14, 70, 'ADDRESS'), (78, 102, 'EMAIL')]}),

    ("Please contact wm5zue66dm7uthnymx@gmail.com for queries.",
     {"entities": [(15, 43, 'EMAIL')]}),

    ("Card 4672402859134471 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("User registered with hohxrs1qkkvb6@gmail.com.",
     {"entities": [(21, 44, 'EMAIL')]}),

    ("Disputed transaction on card 5332465350616123.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Verify card 6546532052499878 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Customer lives at 53-A, Dev Nagar, Pitambara Enclave, Pathoriya, Bansal Colony, Jhansi.",
     {"entities": [(18, 86, 'ADDRESS')]}),

    ("OTP sent to zq490plk5ux71mfs@gmail.com.",
     {"entities": [(12, 38, 'EMAIL')]}),

    ("Payment failed for card 341337490154264.",
     {"entities": [(24, 39, 'CREDIT_CARD')]}),

    ("Pallavi Joshi card 4828752212839706 blocked.",
     {"entities": [(0, 13, 'PERSON'), (19, 35, 'CREDIT_CARD')]}),

    ("Email pk0h6r804h4_6v185t@gmail.com not verified.",
     {"entities": [(6, 34, 'EMAIL')]}),

    ("Recovery email set to wq30_omld1hu0dodz5k@gmail.com.",
     {"entities": [(22, 51, 'EMAIL')]}),

    ("Customer lives at E 48/4, Pocket D, Okhla Phase II, Okhla Industrial Estate, New Delhi.",
     {"entities": [(18, 86, 'ADDRESS')]}),

    ("Recovery email set to emjxv.5@gmail.com.",
     {"entities": [(22, 39, 'EMAIL')]}),

    ("Invoice to be sent at C879+6R9, Purab Sharira, Kaushambi, Uttar Pradesh 212214.",
     {"entities": [(22, 78, 'ADDRESS')]}),

    ("Recovery email set to ia70fyh3jwd@gmail.com.",
     {"entities": [(22, 43, 'EMAIL')]}),

    ("Billing address: 1st floor, Sushma Hospital, A-139, V.C. Rd, Ashiyana Colony, Moradabad.",
     {"entities": [(17, 87, 'ADDRESS')]}),

    ("Property located at near CP Palace, Shivaji Nagar, Jhansi, Uttar Pradesh 284001.",
     {"entities": [(20, 79, 'ADDRESS')]}),

    ("Customer lives at VW9G+7V2, Mukarimnagar, Daliganj, Lucknow, Uttar Pradesh 226007.",
     {"entities": [(18, 81, 'ADDRESS')]}),

    ("Send OTP to x182ce4jexf8@gmail.com immediately.",
     {"entities": [(12, 34, 'EMAIL')]}),

    ("Account linked to v9aim7cfy2hry5u9afs@gmail.com.",
     {"entities": [(18, 47, 'EMAIL')]}),

    ("User registered with t5s8f0x2t7azgb9@gmail.com.",
     {"entities": [(21, 46, 'EMAIL')]}),

    ("Send report to l4f4_v2paptq@gmail.com.",
     {"entities": [(15, 37, 'EMAIL')]}),

    ("Send documents to 595J+9Q6, Suhag Nagar Rd, Opp.CIC Building, Sector 1, Suhag Nagar.",
     {"entities": [(18, 83, 'ADDRESS')]}),

    ("Account linked to jmc_7zp3hpdeay6b7aa@gmail.com.",
     {"entities": [(18, 47, 'EMAIL')]}),

    ("Account linked to fspth7mcyjpn@gmail.com.",
     {"entities": [(18, 40, 'EMAIL')]}),

    ("New card 4963864029983660 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Please ship to Besides Zudio, A-64, Indira Nagar Main Rd, Northern Railway.",
     {"entities": [(15, 74, 'ADDRESS')]}),

    ("Send documents to C5V9+J9P, Unnamed Road, Jabdahi, Jewnar, Uttar Pradesh 271201.",
     {"entities": [(18, 79, 'ADDRESS')]}),

    ("Property located at Mirzahadi Pura, Mau, Uttar Pradesh 275101.",
     {"entities": [(20, 61, 'ADDRESS')]}),

    ("Registered address: 9GXW+8P8, Balibhadrapur, Eiyatee Or Iyaee, Bhadohi Nagar Palika.",
     {"entities": [(20, 83, 'ADDRESS')]}),

    ("Branch office at V6G8+9H3, Ballia - Bansdih Rd, Bansdih, Maniyar Chak, Uttar Pradesh 277202.",
     {"entities": [(17, 91, 'ADDRESS')]}),

    ("Invoice to be sent at Q224+V9V, Kanhara, Uttar Pradesh 231216.",
     {"entities": [(22, 61, 'ADDRESS')]}),

    ("Send OTP to bh43uei@gmail.com immediately.",
     {"entities": [(12, 29, 'EMAIL')]}),

    ("Card 5519195434757820 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("OTP sent to afc0it@gmail.com.",
     {"entities": [(12, 28, 'EMAIL')]}),

    ("Recovery email set to q3aob1rn4q0z@gmail.com.",
     {"entities": [(22, 44, 'EMAIL')]}),

    ("Block card 4624247324185036 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Disputed transaction on card 376311323672724.",
     {"entities": [(29, 44, 'CREDIT_CARD')]}),

    ("Payment failed for card 371129838530650.",
     {"entities": [(24, 39, 'CREDIT_CARD')]}),

    ("Bill sent to b2zqd.oc9dey3y7g5tq@gmail.com for card 6069178255167485.",
     {"entities": [(13, 42, 'EMAIL'), (52, 68, 'CREDIT_CARD')]}),

    ("Send documents to RJ7W+99Q, Chamunda Devi Rd, Tarora, Kasganj, Uttar Pradesh 207123.",
     {"entities": [(18, 83, 'ADDRESS')]}),

    ("Customer Deepika Nair lives at near Water Tank, Preetam Nagar, MIG Preetam Nagar Colony, Dhoomanganj. Contact: u7j4z972136662x2qx4@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 100, 'ADDRESS'), (111, 140, 'EMAIL')]}),

    ("Send OTP to b.av3exhh@gmail.com immediately.",
     {"entities": [(12, 31, 'EMAIL')]}),

    ("Sanjay Gupta used card 6082566511816841 at PQJG+38J, Hans Gali, Gopi Pura, Ganga Nagar Colony, Hapur.",
     {"entities": [(0, 12, 'PERSON'), (23, 39, 'CREDIT_CARD'), (43, 100, 'ADDRESS')]}),

    ("Disputed transaction on card 373618233620877.",
     {"entities": [(29, 44, 'CREDIT_CARD')]}),

    ("Account linked to th72a86_p68ya6jynn2m@gmail.com.",
     {"entities": [(18, 48, 'EMAIL')]}),

    ("New card 4814953816179376 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Registered address: VWWW+W39, Pratapgarh, Uttar Pradesh 230002.",
     {"entities": [(20, 62, 'ADDRESS')]}),

    ("Please contact sabvuzmfg3h.ejwi.0bq@gmail.com for queries.",
     {"entities": [(15, 45, 'EMAIL')]}),

    ("Send report to lqmexpl7brft_v@gmail.com.",
     {"entities": [(15, 39, 'EMAIL')]}),

    ("Card 5466743468919368 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Card 377073397336450 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Billing address: 7VVP+R8H, Makaniya Purva, Mahoba, Uttar Pradesh 210427.",
     {"entities": [(17, 71, 'ADDRESS')]}),

    ("Card 6057630376735240 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Send statement to swmjnduh4uxbj@gmail.com for Deepika Nair.",
     {"entities": [(18, 41, 'EMAIL'), (46, 58, 'PERSON')]}),

    ("Please contact xdl2afinp@gmail.com for queries.",
     {"entities": [(15, 34, 'EMAIL')]}),

    ("Send documents to VW3Q+F6, Shahjahanpur, Ahmadpur Niwazpur, Uttar Pradesh 242406.",
     {"entities": [(18, 80, 'ADDRESS')]}),

    ("New card 4145686984894085 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Send statement to xvacyxq9w1gj@gmail.com for Ramesh Babu.",
     {"entities": [(18, 40, 'EMAIL'), (45, 56, 'PERSON')]}),

    ("Card 6598313587156196 linked to ok56trx2u@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 51, 'EMAIL')]}),

    ("Payment failed for card 6588418513608661.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Send documents to CQMC+9VP, Ashrafpur Kichhauchha, Uttar Pradesh 224155.",
     {"entities": [(18, 71, 'ADDRESS')]}),

    ("Tarun Khanna card 5449583311776024 blocked.",
     {"entities": [(0, 12, 'PERSON'), (18, 34, 'CREDIT_CARD')]}),

    ("Rohit Mehta card 342474552753685 blocked.",
     {"entities": [(0, 11, 'PERSON'), (17, 32, 'CREDIT_CARD')]}),

    ("Block card 5227381431631005 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Send documents to Holi Chowk, Vijay Nagar Colony, Professor Colony, Budaun.",
     {"entities": [(18, 74, 'ADDRESS')]}),

    ("Send statement to r3ic08n23@gmail.com for Priya Singh.",
     {"entities": [(18, 37, 'EMAIL'), (42, 53, 'PERSON')]}),

    ("Property located at Q592+5V7, Harpur, Ballia, Uttar Pradesh 277001.",
     {"entities": [(20, 66, 'ADDRESS')]}),

    ("Deepika Nair at by pass, Ratanpur, Akbarpur, Uttar Pradesh 224122, email si5_dfbrxs3yqsl6na63@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 65, 'ADDRESS'), (73, 103, 'EMAIL')]}),

    ("Registered address: RQJM+WPP, Road, Peer Gali, Moradabad, Uttar Pradesh 244001.",
     {"entities": [(20, 78, 'ADDRESS')]}),

    ("Invoice to be sent at Gali no.1, Santosh Nagar, Raipura Rd, in front of Manoj Book Centre.",
     {"entities": [(22, 89, 'ADDRESS')]}),

    ("Card 5438845276397857 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Delivery address is 624W+24C, Dr Ambedkar Nagar, Trans Yamuna Colony, Agra.",
     {"entities": [(20, 74, 'ADDRESS')]}),

    ("Email ce6i40@gmail.com not verified.",
     {"entities": [(6, 22, 'EMAIL')]}),

    ("Billing address: J6HG+X6W, Kanchenjunga Building, Barakhamba, New Delhi, Delhi 110001.",
     {"entities": [(17, 85, 'ADDRESS')]}),

    ("Statement sent to vqx93nsm349wzj@gmail.com successfully.",
     {"entities": [(18, 42, 'EMAIL')]}),

    ("Property located at MW7W+X57, Village-Ramupur post- khoriya Bazar district.",
     {"entities": [(20, 74, 'ADDRESS')]}),

    ("Registered address: 9JH6+9C9, Bhadohi Rd, Parsotam Patti, Manikpur, Uttar Pradesh 221402.",
     {"entities": [(20, 88, 'ADDRESS')]}),

    ("Card 6088799484188549 linked to zw58j87@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 49, 'EMAIL')]}),

    ("Delivery address is LRP Rd, Maharaj Nagar, Lakhimpur, Uttar Pradesh 262701.",
     {"entities": [(20, 74, 'ADDRESS')]}),

    ("Bill sent to ag4v21@gmail.com for card 4392025304278628.",
     {"entities": [(13, 29, 'EMAIL'), (39, 55, 'CREDIT_CARD')]}),

    ("User registered with ftgckfgr1erepg.8db44@gmail.com.",
     {"entities": [(21, 51, 'EMAIL')]}),

    ("Send report to eo0rd@gmail.com.",
     {"entities": [(15, 30, 'EMAIL')]}),

    ("Send report to doooircqjphnjx7@gmail.com.",
     {"entities": [(15, 40, 'EMAIL')]}),

    ("Verify card 372653064819150 with bank.",
     {"entities": [(12, 27, 'CREDIT_CARD')]}),

    ("OTP sent to whk45jmjmlgy4853z_d@gmail.com.",
     {"entities": [(12, 41, 'EMAIL')]}),

    ("Registered address: HJ2W+PR5, Punjapura, Etah, Ghilaua, Uttar Pradesh 207001.",
     {"entities": [(20, 76, 'ADDRESS')]}),

    ("Send OTP to wv680unv_iw34kmap@gmail.com immediately.",
     {"entities": [(12, 39, 'EMAIL')]}),

    ("New card 349913083538612 issued to customer.",
     {"entities": [(9, 24, 'CREDIT_CARD')]}),

    ("Property located at Uttar Pradesh raebareli salon, Jai maa bhawani, deeh, Birnawa.",
     {"entities": [(20, 81, 'ADDRESS')]}),

    ("Property located at Janki Kund, Chitrakoot, Madhya Pradesh 485334.",
     {"entities": [(20, 65, 'ADDRESS')]}),

    ("Card 346135785719745 linked to this account.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Customer lives at Badli Katra, Girdhar Ka Chauraha, Wellesley Ganj, Mirzapur.",
     {"entities": [(18, 76, 'ADDRESS')]}),

    ("Payment failed for card 4706211774534723.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Payment failed for card 4502681193201784.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Notification sent to bhku1r4znt3_2tpcpx@gmail.com.",
     {"entities": [(21, 49, 'EMAIL')]}),

    ("Card 5495701419322840 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Notification sent to y.rmgew@gmail.com.",
     {"entities": [(21, 38, 'EMAIL')]}),

    ("Rahul Sharma used card 343678865912163 at GC7J+VFM, Magarwara, Maswasi, Uttar Pradesh 209862.",
     {"entities": [(0, 12, 'PERSON'), (23, 38, 'CREDIT_CARD'), (42, 92, 'ADDRESS')]}),

    ("User registered with f47476af1_qw@gmail.com.",
     {"entities": [(21, 43, 'EMAIL')]}),

    ("Billing address: W5CP+WW4, Lakhpedabagh, Barabanki, Barel, Uttar Pradesh 225001.",
     {"entities": [(17, 79, 'ADDRESS')]}),

    ("Delivery address is 73GM+HQQ, SH 1A, Mahariya, Naugarh, Tetri Bazar, Uttar Pradesh 272207.",
     {"entities": [(20, 89, 'ADDRESS')]}),

    ("Account linked to r5tv0p@gmail.com.",
     {"entities": [(18, 34, 'EMAIL')]}),

    ("Send OTP to lz6vb2cypm6yr@gmail.com immediately.",
     {"entities": [(12, 35, 'EMAIL')]}),

    ("New card 4036046876765633 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Amit Kumar card 5299601532289275 blocked.",
     {"entities": [(0, 10, 'PERSON'), (16, 32, 'CREDIT_CARD')]}),

    ("Verify card 376242628867210 with bank.",
     {"entities": [(12, 27, 'CREDIT_CARD')]}),

    ("Please ship to 595R+9XG, Rehna Rd, Bypass Road, Sarswati Nagar.",
     {"entities": [(15, 62, 'ADDRESS')]}),

    ("Card 372122080271696 was used at ATM.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Registered address: PPFR+XX7, Preet Vihar, Hapur, Uttar Pradesh 245101.",
     {"entities": [(20, 70, 'ADDRESS')]}),

    ("Transaction on card 6082026403177010 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Statement sent to wxd8amryyx_6yp5p@gmail.com successfully.",
     {"entities": [(18, 44, 'EMAIL')]}),

    ("Verify card 349098576734375 with bank.",
     {"entities": [(12, 27, 'CREDIT_CARD')]}),

    ("Card 374913275946143 was used at ATM.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("User registered with t4fnm4i0s@gmail.com.",
     {"entities": [(21, 40, 'EMAIL')]}),

    ("Notification sent to thsdh5gw5@gmail.com.",
     {"entities": [(21, 40, 'EMAIL')]}),

    ("Disputed transaction on card 5200828588495350.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Account linked to k06v37@gmail.com.",
     {"entities": [(18, 34, 'EMAIL')]}),

    ("Property located at 9HWH+RRV khairati khan, Bhikampura, Farrukhabad, Uttar Pradesh 209625.",
     {"entities": [(20, 89, 'ADDRESS')]}),

    ("Property located at FH68+WM5, Khajoor Bagh, Indrapuri, Jhansi, Uttar Pradesh 284002.",
     {"entities": [(20, 83, 'ADDRESS')]}),

    ("Ramesh Babu used card 5495876860746554 at 73HC+PC9, Khajuriya, Naugarh, Uttar Pradesh 272207.",
     {"entities": [(0, 11, 'PERSON'), (22, 38, 'CREDIT_CARD'), (42, 92, 'ADDRESS')]}),

    ("Statement sent to p8mfkk35kzkb@gmail.com successfully.",
     {"entities": [(18, 40, 'EMAIL')]}),

    ("Block card 5323934318489378 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("New card 373598462658747 issued to customer.",
     {"entities": [(9, 24, 'CREDIT_CARD')]}),

    ("Customer lives at NIFD campus, Ramghat Rd, near janakpuri water tank, Kishanpur, J-8.",
     {"entities": [(18, 84, 'ADDRESS')]}),

    ("Email wxj.43vcjoiqekb21z@gmail.com not verified.",
     {"entities": [(6, 34, 'EMAIL')]}),

    ("Send report to bm_52broyk7zfbzg@gmail.com.",
     {"entities": [(15, 41, 'EMAIL')]}),

    ("Delivery address is WQXJ+9PQ, Main Road, Tharbaranganj, Lakhimpur, Uttar Pradesh 262701.",
     {"entities": [(20, 87, 'ADDRESS')]}),

    ("Statement sent to buboabhhn6rbix@gmail.com successfully.",
     {"entities": [(18, 42, 'EMAIL')]}),

    ("Please contact waf_gbgb1jqbcj@gmail.com for queries.",
     {"entities": [(15, 39, 'EMAIL')]}),

    ("New card 4375599301037068 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Transaction on card 5212657275739349 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Block card 4915139103420511 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("New card 340420303098510 issued to customer.",
     {"entities": [(9, 24, 'CREDIT_CARD')]}),

    ("Recovery email set to swc9y6nrixsvgvz@gmail.com.",
     {"entities": [(22, 47, 'EMAIL')]}),

    ("Office is at GFQR+9J4, Ab Nagar, Unnao, Uttar Pradesh 209801.",
     {"entities": [(13, 60, 'ADDRESS')]}),

    ("Send statement to htilouu@gmail.com for Manoj Tiwari.",
     {"entities": [(18, 35, 'EMAIL'), (40, 52, 'PERSON')]}),

    ("Charge card number 345460268539723 for INR 2000.",
     {"entities": [(19, 34, 'CREDIT_CARD')]}),

    ("Ramesh Babu card 346875708595199 blocked.",
     {"entities": [(0, 11, 'PERSON'), (17, 32, 'CREDIT_CARD')]}),

    ("Charge card number 5426102091222969 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Send documents to 164/9, Sandeep Talkies Compound South Civil Lines, Court Rd, Muzaffarnagar.",
     {"entities": [(18, 92, 'ADDRESS')]}),

    ("Card 4819423033539070 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Customer lives at 8233+9VM, Madanpura Rd, Opposite INDIA SAREES, Bangali Tola, Varanasi.",
     {"entities": [(18, 87, 'ADDRESS')]}),

    ("Email x948vunnliyj5ozuwgp@gmail.com not verified.",
     {"entities": [(6, 35, 'EMAIL')]}),

    ("Bill sent to f8608i@gmail.com for card 373457955643518.",
     {"entities": [(13, 29, 'EMAIL'), (39, 54, 'CREDIT_CARD')]}),

    ("Billing address: H9MQ+4J5, अबादगढ़थानाभवन, Shamli, Abadgarh, Uttar Pradesh 247776.",
     {"entities": [(17, 81, 'ADDRESS')]}),

    ("Bill sent to zqxwwb59@gmail.com for card 4680827020989938.",
     {"entities": [(13, 31, 'EMAIL'), (41, 57, 'CREDIT_CARD')]}),

    ("Card 348767416789303 linked to this account.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Geeta Rani used card 5352280386001214 at Rohtak Rd, Shivaji Park, Block S, West Punjabi Bagh, Punjabi Bagh.",
     {"entities": [(0, 10, 'PERSON'), (21, 37, 'CREDIT_CARD'), (41, 106, 'ADDRESS')]}),

    ("OTP sent to k1w6_ancq_z@gmail.com.",
     {"entities": [(12, 33, 'EMAIL')]}),

    ("Send report to xgyzz2jo1mdtl.es9n@gmail.com.",
     {"entities": [(15, 43, 'EMAIL')]}),

    ("Registered address: at District Hospital, near Collectorate, Baghpat, Uttar Pradesh 250619.",
     {"entities": [(20, 90, 'ADDRESS')]}),

    ("Property located at WARD NO. 4, KASIA ROAD RAMKOLA, DIST:, Kushinagar, Uttar Pradesh 274305.",
     {"entities": [(20, 91, 'ADDRESS')]}),

    ("Customer Shruti Desai lives at Sikandra, Kanpur Dehat NH-2A, Bhognipur, Auraiya Road, Kanpur. Contact: cy.rvw3scmx80r@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 92, 'ADDRESS'), (103, 127, 'EMAIL')]}),

    ("Please contact gl2n1mpxd49gk@gmail.com for queries.",
     {"entities": [(15, 38, 'EMAIL')]}),

    ("Send report to l86y9e86it@gmail.com.",
     {"entities": [(15, 35, 'EMAIL')]}),

    ("Delivery address is Phanderi Sadat - Amroha Link Rd, Gulariya, Amroha, Uttar Pradesh 244221.",
     {"entities": [(20, 91, 'ADDRESS')]}),

    ("Card 6575455127235763 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Property located at WF46+MGM, SH 77, Islam Nagar, Amroha, Uttar Pradesh 244221.",
     {"entities": [(20, 78, 'ADDRESS')]}),

    ("Payment failed for card 5235378011325617.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Shruti Desai at CVC6+3HQ, Arail Ghat, Below Naya Pul, Arail Ghat Rd, Naini, Prayagraj, email ix9tmqu@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 85, 'ADDRESS'), (93, 110, 'EMAIL')]}),

    ("Registered address: Indira Colony 2nd, near Sport Stadium, Uttar Pradesh 203001.",
     {"entities": [(20, 79, 'ADDRESS')]}),

    ("OTP sent to l0qmmi5x2b6ftgk220dp@gmail.com.",
     {"entities": [(12, 42, 'EMAIL')]}),

    ("Card 346010021605509 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Account linked to z7ibs5b_i8sgmxw@gmail.com.",
     {"entities": [(18, 43, 'EMAIL')]}),

    ("Tarun Khanna at P398+J2Q, Main Road, Ground Floor, email w.o.6h02m3yht@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 49, 'ADDRESS'), (57, 80, 'EMAIL')]}),

    ("Card 344392758480753 linked to y12hx@gmail.com.",
     {"entities": [(5, 20, 'CREDIT_CARD'), (31, 46, 'EMAIL')]}),

    ("Disputed transaction on card 4030644960901723.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Charge card number 345425918567291 for INR 2000.",
     {"entities": [(19, 34, 'CREDIT_CARD')]}),

    ("Card 6569493060517655 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Payment failed for card 379477898330147.",
     {"entities": [(24, 39, 'CREDIT_CARD')]}),

    ("Card 5430139798234267 linked to p7ivvk@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 48, 'EMAIL')]}),

    ("Shruti Desai used card 5420079014087643 at Am Complex, 226a, Ekta Nagar, Pilibhit, Uttar Pradesh 262001.",
     {"entities": [(0, 12, 'PERSON'), (23, 39, 'CREDIT_CARD'), (43, 103, 'ADDRESS')]}),

    ("Please ship to QPXW+J52, Gandhi Nagar Rd, Pikura Mohalla, Basti, Uttar Pradesh 272001.",
     {"entities": [(15, 85, 'ADDRESS')]}),

    ("Send OTP to b.h87c7.a.3@gmail.com immediately.",
     {"entities": [(12, 33, 'EMAIL')]}),

    ("User registered with ziq_5om1opafmrzw32kj@gmail.com.",
     {"entities": [(21, 51, 'EMAIL')]}),

    ("Card 5285583476209471 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("User registered with fr_7aqjgu_1@gmail.com.",
     {"entities": [(21, 42, 'EMAIL')]}),

    ("Email cbigs2w@gmail.com not verified.",
     {"entities": [(6, 23, 'EMAIL')]}),

    ("Send report to dvkfppl@gmail.com.",
     {"entities": [(15, 32, 'EMAIL')]}),

    ("Email uvfgfbxv4ah9sfsw2jb@gmail.com not verified.",
     {"entities": [(6, 35, 'EMAIL')]}),

    ("Property located at 394, Lucknow Rd, Shahganj, Sadar Bazar, Lok Nagar, Unnao.",
     {"entities": [(20, 76, 'ADDRESS')]}),

    ("Charge card number 6580354480971616 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Customer Suresh Patel lives at 9HV8+PMR, Sarvat Khani, Chedibeer, Bhadohi Nagar Palika. Contact: x9jp8wcbyboe@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 86, 'ADDRESS'), (97, 119, 'EMAIL')]}),

    ("Statement sent to kun5r4jye0uowft@gmail.com successfully.",
     {"entities": [(18, 43, 'EMAIL')]}),

    ("Customer Sunita Verma lives at WC7W+GJX, Daud Sarai Road, P.O. Amroha, Nizampur Garbi. Contact: wawnen47n3s4yyo54@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 85, 'ADDRESS'), (96, 123, 'EMAIL')]}),

    ("Card 343244892137213 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Customer lives at 5VC9+4WR, Unnamed Road, Naya Gaon, Chitrakoot, Madhya Pradesh 485334.",
     {"entities": [(18, 86, 'ADDRESS')]}),

    ("Send statement to gfvp43@gmail.com for Vikram Malhotra.",
     {"entities": [(18, 34, 'EMAIL'), (39, 54, 'PERSON')]}),

    ("New card 6052801568053479 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Delivery address is H NO. 5 K VILLAGE BHABHNAULI BHABHNAULI, Uttar Pradesh 231216.",
     {"entities": [(20, 81, 'ADDRESS')]}),

    ("Send OTP to xv3tkewoxd4scqwb29f@gmail.com immediately.",
     {"entities": [(12, 41, 'EMAIL')]}),

    ("Statement sent to ks6.fi5@gmail.com successfully.",
     {"entities": [(18, 35, 'EMAIL')]}),

    ("Card 5461242589300682 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Charge card number 5444960763899183 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Disputed transaction on card 4218848731283332.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Customer lives at C547+VC8, Pedda, Peda Urf Murtajapur Bulaki, Uttar Pradesh 246701.",
     {"entities": [(18, 83, 'ADDRESS')]}),

    ("Account linked to ubbk7_73lzihi@gmail.com.",
     {"entities": [(18, 41, 'EMAIL')]}),

    ("OTP sent to h7uq3sb.w5l0uaamz@gmail.com.",
     {"entities": [(12, 39, 'EMAIL')]}),

    ("Notification sent to ko2jft4a1eschk6@gmail.com.",
     {"entities": [(21, 46, 'EMAIL')]}),

    ("Invoice to be sent at Ward No. 5, Sheetla Mandir ki Gali, Purab Mohal Rd, Tagore Nagar.",
     {"entities": [(22, 86, 'ADDRESS')]}),

    ("Customer lives at 4/41, Shivlok Colony, Hapur, Uttar Pradesh 245101.",
     {"entities": [(18, 67, 'ADDRESS')]}),

    ("Please contact mwvyn3pz@gmail.com for queries.",
     {"entities": [(15, 33, 'EMAIL')]}),

    ("Notification sent to gsdrageyrlayaho@gmail.com.",
     {"entities": [(21, 46, 'EMAIL')]}),

    ("Delivery address is FMWJ+2VG, Opposite Bhagat Singh Park, Dampier Nagar, Mathura.",
     {"entities": [(20, 80, 'ADDRESS')]}),

    ("Nisha Agarwal card 5188795457471115 blocked.",
     {"entities": [(0, 13, 'PERSON'), (19, 35, 'CREDIT_CARD')]}),

    ("User registered with a9e1f8k@gmail.com.",
     {"entities": [(21, 38, 'EMAIL')]}),

    ("Delivery address is VPO: BAMNAULI, Bamnauli, Uttar Pradesh 250620.",
     {"entities": [(20, 65, 'ADDRESS')]}),

    ("Send OTP to ix9ttis@gmail.com immediately.",
     {"entities": [(12, 29, 'EMAIL')]}),

    ("Payment failed for card 4061920756498954.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Delivery address is QPWQ+G87, Pikura Mohalla, Basti, Uttar Pradesh 272001.",
     {"entities": [(20, 73, 'ADDRESS')]}),

    ("Customer Deepika Nair lives at 157, Chedibeer, Bhadohi Nagar Palika, Piyari, Uttar Pradesh 221401. Contact: ma3ef07sd@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 97, 'ADDRESS'), (108, 127, 'EMAIL')]}),

    ("Office is at Shop No -35, Shopping Center, I P ext.DDA MKT 92, Patparganj, New Delhi.",
     {"entities": [(13, 84, 'ADDRESS')]}),

    ("Please ship to 9HG9+HJV, near Railway Crossing, Mubarakpur Marala, Uttar Pradesh 224235.",
     {"entities": [(15, 87, 'ADDRESS')]}),

    ("Card 5414480717088201 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Property located at WQJQ+V55, Rajajipuram, Moh Nai Basti, Lakhimpur, Uttar Pradesh 262701.",
     {"entities": [(20, 89, 'ADDRESS')]}),

    ("Verify card 5115844966718208 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Delivery address is RQ77+J59, Majhuwameer, Basti Khas, Basti, Uttar Pradesh 272002.",
     {"entities": [(20, 82, 'ADDRESS')]}),

    ("Recovery email set to t9k7n4fju8seaa1@gmail.com.",
     {"entities": [(22, 47, 'EMAIL')]}),

    ("Payment failed for card 5449038488308930.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Customer lives at Q2HF+H7C, Railway Station, National Highway 24, Civil Lines, Rampur.",
     {"entities": [(18, 85, 'ADDRESS')]}),

    ("Verify card 4593126582325086 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Card 5157704392053375 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Branch office at 6WFC+J2Q, MDR 26B, Talib City, Chitrakoot Dham, Uttar Pradesh 210205.",
     {"entities": [(17, 85, 'ADDRESS')]}),

    ("Send report to itzqs@gmail.com.",
     {"entities": [(15, 30, 'EMAIL')]}),

    ("Please contact saim62wpb15mgsxk336@gmail.com for queries.",
     {"entities": [(15, 44, 'EMAIL')]}),

    ("Please contact qvhjc6r@gmail.com for queries.",
     {"entities": [(15, 32, 'EMAIL')]}),

    ("Office is at Unnamed Road, Block A, Ghazipur Dairy Farm, Ghazipur, Gazipur, Delhi.",
     {"entities": [(13, 81, 'ADDRESS')]}),

    ("Block card 6000703015589529 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Send OTP to szqf.n_f3@gmail.com immediately.",
     {"entities": [(12, 31, 'EMAIL')]}),

    ("Office is at 4WHV+W93, Housing Colony, Gonda, Uttar Pradesh 271001.",
     {"entities": [(13, 66, 'ADDRESS')]}),

    ("User registered with io1g6dmu@gmail.com.",
     {"entities": [(21, 39, 'EMAIL')]}),

    ("Card 373907149682280 linked to ne56h6agg1@gmail.com.",
     {"entities": [(5, 20, 'CREDIT_CARD'), (31, 51, 'EMAIL')]}),

    ("Email l2bjh7lz@gmail.com not verified.",
     {"entities": [(6, 24, 'EMAIL')]}),

    ("User registered with obndxoob50g_b@gmail.com.",
     {"entities": [(21, 44, 'EMAIL')]}),

    ("Customer Meena Patel lives at Bulandshahr, Uttar Pradesh 203131. Contact: cfujeir_9uy7s361gh9@gmail.com.",
     {"entities": [(9, 20, 'PERSON'), (30, 63, 'ADDRESS'), (74, 103, 'EMAIL')]}),

    ("Billing address: 321 S, 321 S, Chirag Dilli, New Delhi, Delhi 110017.",
     {"entities": [(17, 68, 'ADDRESS')]}),

    ("Disputed transaction on card 6518680661040869.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Delivery address is 2nd floor Shivam complex ,beside Kanker Khera flyover police choki.",
     {"entities": [(20, 86, 'ADDRESS')]}),

    ("Card 4332455083790569 linked to fyq93sg4e.ncocqlyds9@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 62, 'EMAIL')]}),

    ("Send documents to Bukhari Tola, MDR 75C, Kheri, Uttar Pradesh 262701.",
     {"entities": [(18, 68, 'ADDRESS')]}),

    ("Customer Kiran Bedi lives at J29X+H9M, Basant Bagh, Water Works Colony, Hathras, Uttar Pradesh 204101. Contact: hofoean522mqzluleqf7@gmail.com.",
     {"entities": [(9, 19, 'PERSON'), (29, 101, 'ADDRESS'), (112, 142, 'EMAIL')]}),

    ("Payment failed for card 4515218089313216.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Please contact g5ewlrkjq25h7v98l@gmail.com for queries.",
     {"entities": [(15, 42, 'EMAIL')]}),

    ("User registered with en1dfmh1gx@gmail.com.",
     {"entities": [(21, 41, 'EMAIL')]}),

    ("Card 6510060776667783 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Verify card 5328618894957018 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Property located at A 1/6 Shakti Nagar Extention, Ashok Vihar Rd, near Kali Mata Mandir.",
     {"entities": [(20, 87, 'ADDRESS')]}),

    ("Account linked to vryp8fvts_qgx2cnm@gmail.com.",
     {"entities": [(18, 45, 'EMAIL')]}),

    ("Delivery address is GXR8+F2C, Baraipur, Uttar Pradesh 271845.",
     {"entities": [(20, 60, 'ADDRESS')]}),

    ("Amit Kumar card 374177350203407 blocked.",
     {"entities": [(0, 10, 'PERSON'), (16, 31, 'CREDIT_CARD')]}),

    ("Payment failed for card 4252275049574961.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Email nwuylex.xw5p_28ib7@gmail.com not verified.",
     {"entities": [(6, 34, 'EMAIL')]}),

    ("Send OTP to xxev1_nnj40jy@gmail.com immediately.",
     {"entities": [(12, 35, 'EMAIL')]}),

    ("Card 4817616836284732 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Email afxg9uwlurew21xhe@gmail.com not verified.",
     {"entities": [(6, 33, 'EMAIL')]}),

    ("Notification sent to i3a1fu@gmail.com.",
     {"entities": [(21, 37, 'EMAIL')]}),

    ("Card 4381574170757959 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Send statement to rxn0oy8wjtltg@gmail.com for Pallavi Joshi.",
     {"entities": [(18, 41, 'EMAIL'), (46, 59, 'PERSON')]}),

    ("Send report to c7k_zpojdd0@gmail.com.",
     {"entities": [(15, 36, 'EMAIL')]}),

    ("Block card 342717149898533 immediately.",
     {"entities": [(11, 26, 'CREDIT_CARD')]}),

    ("Send report to je0kzkpuldoob63jwoy@gmail.com.",
     {"entities": [(15, 44, 'EMAIL')]}),

    ("Recovery email set to k31rd_r@gmail.com.",
     {"entities": [(22, 39, 'EMAIL')]}),

    ("Amit Kumar at 229, shri nagar, Jalesar Rd, Firozabad, Uttar Pradesh 283203, email krl11475d41@gmail.com.",
     {"entities": [(0, 10, 'PERSON'), (14, 74, 'ADDRESS'), (82, 103, 'EMAIL')]}),

    ("Customer Ramesh Babu lives at 423A, Vaishnavpuram, Huzoorpur Road, Bahraich, Uttar Pradesh 271801. Contact: pwzm4fvnlsvl@gmail.com.",
     {"entities": [(9, 20, 'PERSON'), (30, 97, 'ADDRESS'), (108, 130, 'EMAIL')]}),

    ("Block card 6048233632404347 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Customer lives at Ground & 1st Floor, Property No, 559 D, Azad Road, Amroha.",
     {"entities": [(18, 75, 'ADDRESS')]}),

    ("Send documents to PMJF+R36 Railway Station, Nera, below overbridge, Naiganj, Olandganj.",
     {"entities": [(18, 86, 'ADDRESS')]}),

    ("Please contact djqmljel53.o@gmail.com for queries.",
     {"entities": [(15, 37, 'EMAIL')]}),

    ("Statement sent to g41ddg70h10bd3rbtf@gmail.com successfully.",
     {"entities": [(18, 46, 'EMAIL')]}),

    ("Card 5560682888531649 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Office is at Q2XC+8R6, Mohsin -E- Azam Colony, Civil Lines, Rampur, Uttar Pradesh 244901.",
     {"entities": [(13, 88, 'ADDRESS')]}),

    ("Bill sent to cihxsaa@gmail.com for card 378137441169446.",
     {"entities": [(13, 30, 'EMAIL'), (40, 55, 'CREDIT_CARD')]}),

    ("Customer Sunita Verma lives at Khasra no. 187 Min, Kamakhya Devi, Ladli Prasad Mandir, Upper Ground Floor. Contact: xujje6ls10qq4xb50phg@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 105, 'ADDRESS'), (116, 146, 'EMAIL')]}),

    ("Suresh Patel used card 6540961026752772 at 3, 3, Bhullanpur, Varanasi, Lakhanpur, Uttar Pradesh 221107.",
     {"entities": [(0, 12, 'PERSON'), (23, 39, 'CREDIT_CARD'), (43, 102, 'ADDRESS')]}),

    ("Billing address: Kalana Gaharwar, Uttar Pradesh 231303.",
     {"entities": [(17, 54, 'ADDRESS')]}),

    ("Card 6064952973811126 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Charge card number 4844359898252179 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Send report to bn1mna2q8588n1lx@gmail.com.",
     {"entities": [(15, 41, 'EMAIL')]}),

    ("Send OTP to aq3sd1@gmail.com immediately.",
     {"entities": [(12, 28, 'EMAIL')]}),

    ("Send statement to m94evi4mjmaa6x@gmail.com for Neha Joshi.",
     {"entities": [(18, 42, 'EMAIL'), (47, 57, 'PERSON')]}),

    ("OTP sent to dkrnlls@gmail.com.",
     {"entities": [(12, 29, 'EMAIL')]}),

    ("Send statement to rtz8ivo2j2v_4r4ru@gmail.com for Sanjay Gupta.",
     {"entities": [(18, 45, 'EMAIL'), (50, 62, 'PERSON')]}),

    ("Notification sent to q.tgw2odihiudc2@gmail.com.",
     {"entities": [(21, 46, 'EMAIL')]}),

    ("Deepika Nair used card 372820946229770 at Ghazipur Nursing Home PVT LTD Prakash Nagar, Bhutaiyatad, NH 29, Ghazipur.",
     {"entities": [(0, 12, 'PERSON'), (23, 38, 'CREDIT_CARD'), (42, 115, 'ADDRESS')]}),

    ("Bill sent to xtda0lkkwrrd0@gmail.com for card 5252086770478635.",
     {"entities": [(13, 36, 'EMAIL'), (46, 62, 'CREDIT_CARD')]}),

    ("User registered with v.s.888zha5u1b1_85@gmail.com.",
     {"entities": [(21, 49, 'EMAIL')]}),

    ("Registered address: Matoshri Plaza, Siddhivinayak Rd, Apte Ghat, Somwar Peth, Pune, Chitrakoot.",
     {"entities": [(20, 94, 'ADDRESS')]}),

    ("Card 346138535720916 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Verify card 5182353184773430 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Statement sent to xpaj8phq0yu4pxtsvm@gmail.com successfully.",
     {"entities": [(18, 46, 'EMAIL')]}),

    ("Account linked to mgd9tlelryi3c@gmail.com.",
     {"entities": [(18, 41, 'EMAIL')]}),

    ("Verify card 378015848257309 with bank.",
     {"entities": [(12, 27, 'CREDIT_CARD')]}),

    ("Branch office at 672, Mathura Bypass, Road, NH-2, Sikandra, Agra, Uttar Pradesh 282007.",
     {"entities": [(17, 86, 'ADDRESS')]}),

    ("Send OTP to l.mk0hm.vz8xeh72@gmail.com immediately.",
     {"entities": [(12, 38, 'EMAIL')]}),

    ("Delivery address is GAUR GLOBAL VILLAGE, E Block, Crossings Republik Rd, Crossings Republik.",
     {"entities": [(20, 91, 'ADDRESS')]}),

    ("User registered with pp71i0crjj8_xe@gmail.com.",
     {"entities": [(21, 45, 'EMAIL')]}),

    ("Invoice to be sent at Sai City Udaypura Farrukhabad Road, NH92, Etawah, Uttar Pradesh 206001.",
     {"entities": [(22, 92, 'ADDRESS')]}),

    ("Card 5493624146506250 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Please ship to 6B, KHATUSHYAM PLAZA, Accher, RHO I, Noida, Greater Noida.",
     {"entities": [(15, 72, 'ADDRESS')]}),

    ("New card 378925949215795 issued to customer.",
     {"entities": [(9, 24, 'CREDIT_CARD')]}),

    ("Statement sent to sz1talowacs@gmail.com successfully.",
     {"entities": [(18, 39, 'EMAIL')]}),

    ("Customer Sunita Verma lives at C5JQ+MQW, Kaithi Rd, Gurera, Balua, Pura, Uttar Pradesh 221114. Contact: ctghwrtctkyjz3@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 93, 'ADDRESS'), (104, 128, 'EMAIL')]}),

    ("Send OTP to b9_ns_oao@gmail.com immediately.",
     {"entities": [(12, 31, 'EMAIL')]}),

    ("Priya Singh card 344967056718389 blocked.",
     {"entities": [(0, 11, 'PERSON'), (17, 32, 'CREDIT_CARD')]}),

    ("Branch office at Panchkosi Parikrama Marg, Ranopali (Mohabra, Road, Ayodhya.",
     {"entities": [(17, 75, 'ADDRESS')]}),

    ("Transaction on card 6559003706268536 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Account linked to crtuz.5kf1du6yc44ny@gmail.com.",
     {"entities": [(18, 47, 'EMAIL')]}),

    ("Disputed transaction on card 5446214318099423.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Notification sent to a5373y@gmail.com.",
     {"entities": [(21, 37, 'EMAIL')]}),

    ("Office is at Kathauli, Uttar Pradesh 207001.",
     {"entities": [(13, 43, 'ADDRESS')]}),

    ("User registered with ph1cpj@gmail.com.",
     {"entities": [(21, 37, 'EMAIL')]}),

    ("User registered with st0llrd3b2@gmail.com.",
     {"entities": [(21, 41, 'EMAIL')]}),

    ("Card 347164534974430 linked to hf6va5r4ko4qis9lg@gmail.com.",
     {"entities": [(5, 20, 'CREDIT_CARD'), (31, 58, 'EMAIL')]}),

    ("Send OTP to oix56d2_pvi@gmail.com immediately.",
     {"entities": [(12, 33, 'EMAIL')]}),

    ("Please ship to Nagar Palika, 2/1/1828, Railway Rd, New Shivpuri, Hapur.",
     {"entities": [(15, 70, 'ADDRESS')]}),

    ("Delivery address is A,69, public school road, near Manoj Sweets, Gandhi Nagar, Moradabad.",
     {"entities": [(20, 88, 'ADDRESS')]}),

    ("Email scy8lg@gmail.com not verified.",
     {"entities": [(6, 22, 'EMAIL')]}),

    ("Send OTP to qb.x4ravbe3i47y84f0e@gmail.com immediately.",
     {"entities": [(12, 42, 'EMAIL')]}),

    ("Delivery address is Guest House, Shastri Setu, near Hindal Co, Putlighar, Mirzapur.",
     {"entities": [(20, 82, 'ADDRESS')]}),

    ("Recovery email set to li7ewmf73@gmail.com.",
     {"entities": [(22, 41, 'EMAIL')]}),

    ("Sunita Verma at 738F+9MX, Civil Line, Sultanpur, Uttar Pradesh 228001, email kqnd.7gwf@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 69, 'ADDRESS'), (77, 96, 'EMAIL')]}),

    ("Account linked to t8guj@gmail.com.",
     {"entities": [(18, 33, 'EMAIL')]}),

    ("Recovery email set to y3fqvbpcmhi80@gmail.com.",
     {"entities": [(22, 45, 'EMAIL')]}),

    ("Please ship to R3P6+8P3, Parasrampur, Uttar Pradesh 230304.",
     {"entities": [(15, 58, 'ADDRESS')]}),

    ("Customer lives at 1/691, Paswan Mohalla Gali, Ramgulam Tola, Deoria, Uttar Pradesh 274001.",
     {"entities": [(18, 89, 'ADDRESS')]}),

    ("Statement sent to zg75ndmhtep@gmail.com successfully.",
     {"entities": [(18, 39, 'EMAIL')]}),

    ("Statement sent to q3l9ecuiqbdc61pcm@gmail.com successfully.",
     {"entities": [(18, 45, 'EMAIL')]}),

    ("Block card 5514391614336874 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Customer Tarun Khanna lives at 25VP+H6P, Sidhari, Azamgarh, Uttar Pradesh 276001. Contact: l0v961ouvkwbw1eawkc4@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 80, 'ADDRESS'), (91, 121, 'EMAIL')]}),

    ("User registered with a1oq_0vy7at7kpu7@gmail.com.",
     {"entities": [(21, 47, 'EMAIL')]}),

    ("Bill sent to w3ygcazu1.nbcn@gmail.com for card 6558728872123022.",
     {"entities": [(13, 37, 'EMAIL'), (47, 63, 'CREDIT_CARD')]}),

    ("Transaction on card 4786238049757380 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("New card 346736022927963 issued to customer.",
     {"entities": [(9, 24, 'CREDIT_CARD')]}),

    ("Card 6568236144816320 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Registered address: B 46, Street No. 7, nearby Shiv Mandir, New Modern Shahdara, Shahdara.",
     {"entities": [(20, 89, 'ADDRESS')]}),

    ("Payment failed for card 341645617756644.",
     {"entities": [(24, 39, 'CREDIT_CARD')]}),

    ("Customer lives at PMGM+6FH, Jaunpur, Uttar Pradesh 222002.",
     {"entities": [(18, 57, 'ADDRESS')]}),

    ("Shruti Desai used card 4798395293856966 at RQC8+2Q5, Unnamed Road, Jamohara, Basti, Uttar Pradesh 272002.",
     {"entities": [(0, 12, 'PERSON'), (23, 39, 'CREDIT_CARD'), (43, 104, 'ADDRESS')]}),

    ("Recovery email set to b7wr_j0yg.l@gmail.com.",
     {"entities": [(22, 43, 'EMAIL')]}),

    ("Statement sent to wf3esxq1m_szbl7wj@gmail.com successfully.",
     {"entities": [(18, 45, 'EMAIL')]}),

    ("Registered address: P6HC+CG7, Mahadev Gali 14A, Wazirabad, New Delhi, Delhi, 110084.",
     {"entities": [(20, 83, 'ADDRESS')]}),

    ("Card 6543190020961694 linked to mctkie23irohw27k31h@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 61, 'EMAIL')]}),

    ("Statement sent to fu3mh1bto.hnz7@gmail.com successfully.",
     {"entities": [(18, 42, 'EMAIL')]}),

    ("Customer Shruti Desai lives at Bus Stand, near Garg Dharam Kanta Sisoli, Punjabi Colony, Shamli. Contact: ri7hin0u@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 95, 'ADDRESS'), (106, 124, 'EMAIL')]}),

    ("Delivery address is R26H+69F Infront of taj hotel, near jamia tul maarif, Kuncha Lala Miyan.",
     {"entities": [(20, 91, 'ADDRESS')]}),

    ("Property located at PMXV+GP6, Balua Ghat, Rizwikhan, Jaunpur, Uttar Pradesh 222001.",
     {"entities": [(20, 82, 'ADDRESS')]}),

    ("Charge card number 4967447468575057 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Card 4408659164260410 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Customer Sunita Verma lives at Syed Isa, 1, Aligarh Bypass Rd, Wadi E Ismaiel, Iqra Colony, Dhourra Mafi. Contact: xuluon3@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 104, 'ADDRESS'), (115, 132, 'EMAIL')]}),

    ("Verify card 6074571371285863 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Statement sent to psoc07i.p_hsy@gmail.com successfully.",
     {"entities": [(18, 41, 'EMAIL')]}),

    ("Geeta Rani used card 4701307252680194 at 1/256 (A), GOLAGHAT, SAHITYANAKA RAMNAGAR, Mirzapur - Varanasi Rd.",
     {"entities": [(0, 10, 'PERSON'), (21, 37, 'CREDIT_CARD'), (41, 106, 'ADDRESS')]}),

    ("Card 370740093271600 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Card 378953708669966 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Branch office at 3, Madhuvan Vatika, Baghmoola Chauraha, near BJP Office, Nagla Emliya.",
     {"entities": [(17, 86, 'ADDRESS')]}),

    ("Property located at S/O, MOHAMMAD IRFAN KHAN HOUSE, good bakery church compound, Civil Line.",
     {"entities": [(20, 91, 'ADDRESS')]}),

    ("Send statement to wtccmq5untn8sz@gmail.com for Deepika Nair.",
     {"entities": [(18, 42, 'EMAIL'), (47, 59, 'PERSON')]}),

    ("Disputed transaction on card 4177595351701075.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Branch office at Plot No 1/145-A, W Ave Rd, West Punjabi Bagh, Punjabi Bagh, New Delhi.",
     {"entities": [(17, 86, 'ADDRESS')]}),

    ("Nisha Agarwal at 4HV9+Q8F, Jaiprakashnagar, Anarutia, Maharajganj, Uttar Pradesh 273303, email l83z.nkxew@gmail.com.",
     {"entities": [(0, 13, 'PERSON'), (17, 87, 'ADDRESS'), (95, 115, 'EMAIL')]}),

    ("Card 4362703472461390 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Card 5556269253978467 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Notification sent to gwqhj2bbsj6@gmail.com.",
     {"entities": [(21, 42, 'EMAIL')]}),

    ("Send report to mtpmb4s@gmail.com.",
     {"entities": [(15, 32, 'EMAIL')]}),

    ("Customer Rekha Iyer lives at 352C+945, Purana Pul, Harbanshpur, Uttar Pradesh 276001. Contact: dusstap6e1sp.pzjel@gmail.com.",
     {"entities": [(9, 19, 'PERSON'), (29, 84, 'ADDRESS'), (95, 123, 'EMAIL')]}),

    ("Transaction on card 6539865643263259 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Send OTP to ka1h04ip2twc@gmail.com immediately.",
     {"entities": [(12, 34, 'EMAIL')]}),

    ("Invoice to be sent at W39C+3GW, Shafi Rd, Purani Chungi, Saheb Bagh, Aligarh.",
     {"entities": [(22, 76, 'ADDRESS')]}),

    ("Account linked to s6bmjmvll7tbhg244bl@gmail.com.",
     {"entities": [(18, 47, 'EMAIL')]}),

    ("Disputed transaction on card 4798821144379109.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Property located at FP95+X2R, Unnamed Road, Civil Lines South, Muzaffarnagar.",
     {"entities": [(20, 76, 'ADDRESS')]}),

    ("Billing address: C5CG+6RJ, Sir Syed Nagar Colony, Nipkauni Rd, Balrampur.",
     {"entities": [(17, 72, 'ADDRESS')]}),

    ("Notification sent to pwgho@gmail.com.",
     {"entities": [(21, 36, 'EMAIL')]}),

    ("Card 4476408557580380 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Statement sent to crb9v_9jlr.23@gmail.com successfully.",
     {"entities": [(18, 41, 'EMAIL')]}),

    ("New card 6040081269247211 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Customer lives at 9HG3+393, Bhadohi Nagar Palika, Uttar Pradesh 221401.",
     {"entities": [(18, 70, 'ADDRESS')]}),

    ("Block card 4358071969304954 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Card 4431477921305748 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Notification sent to n3fqy4q.c1y@gmail.com.",
     {"entities": [(21, 42, 'EMAIL')]}),

    ("Send report to bbc4yrbg5.46or71dg8@gmail.com.",
     {"entities": [(15, 44, 'EMAIL')]}),

    ("Statement sent to f_lm_._7@gmail.com successfully.",
     {"entities": [(18, 36, 'EMAIL')]}),

    ("Send documents to V33G+VMR, Agra Rd, Kalyan Puram, Aligarh, Uttar Pradesh 202001.",
     {"entities": [(18, 80, 'ADDRESS')]}),

    ("Billing address: 73JP+426, Tetri Bazar Town, Naugarh, Uttar Pradesh 272207.",
     {"entities": [(17, 74, 'ADDRESS')]}),

    ("Deepika Nair used card 6579744434595203 at Village Rasoolpur, Post, Sahsapur, Uttar Pradesh 261001.",
     {"entities": [(0, 12, 'PERSON'), (23, 39, 'CREDIT_CARD'), (43, 98, 'ADDRESS')]}),

    ("Email id3sgz@gmail.com not verified.",
     {"entities": [(6, 22, 'EMAIL')]}),

    ("Customer lives at XP8M+M5J SKYLARK COMPLEX, Garh Rd, near HARMONY HOTEL, Janta Nagar.",
     {"entities": [(18, 84, 'ADDRESS')]}),

    ("Account linked to i2o5ei_0@gmail.com.",
     {"entities": [(18, 36, 'EMAIL')]}),

    ("Customer lives at MGR9+PG5, Opposite judicial court complex, Hamirpur, Himachal Pradesh.",
     {"entities": [(18, 87, 'ADDRESS')]}),

    ("Verify card 346106879062122 with bank.",
     {"entities": [(12, 27, 'CREDIT_CARD')]}),

    ("Card 340714062083337 linked to this account.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Please contact zn42m@gmail.com for queries.",
     {"entities": [(15, 30, 'EMAIL')]}),

    ("Office is at WGVV+55F, Vasant Vihar, Saharanpur, Uttar Pradesh 247001.",
     {"entities": [(13, 69, 'ADDRESS')]}),

    ("Office is at Indraprastha Apartments, E-61, Pocket 1, Sector 14, Rohini, Delhi, 110085.",
     {"entities": [(13, 86, 'ADDRESS')]}),

    ("Billing address: Khajuriya Rd, Khajuriya, Naugarh, Uttar Pradesh 272203.",
     {"entities": [(17, 71, 'ADDRESS')]}),

    ("Kiran Bedi used card 5211878233006867 at Paryavaran Complex, C-108, near Mother Dairy, nearby Areas Saidulajab.",
     {"entities": [(0, 10, 'PERSON'), (21, 37, 'CREDIT_CARD'), (41, 110, 'ADDRESS')]}),

    ("Billing address: Nand Vihar, Sector 16A, Dwarka, Delhi, 110078.",
     {"entities": [(17, 62, 'ADDRESS')]}),

    ("Recovery email set to agla6dhho03at1b62kw@gmail.com.",
     {"entities": [(22, 51, 'EMAIL')]}),

    ("Notification sent to do0y5ru@gmail.com.",
     {"entities": [(21, 38, 'EMAIL')]}),

    ("Customer lives at G84V+QJ5, Sarvodaya Nagar, Mawai Buzurg, Uttar Pradesh 210001.",
     {"entities": [(18, 79, 'ADDRESS')]}),

    ("Please ship to 7XXC+CHV, Manduwadih, Varanasi, Uttar Pradesh 221103.",
     {"entities": [(15, 67, 'ADDRESS')]}),

    ("Branch office at GC7M+48V, Kulesara, Noida, Uttar Pradesh 201305.",
     {"entities": [(17, 64, 'ADDRESS')]}),

    ("Billing address: 187, opposite Reliance tower, Qazipur Khurd, Gorakhpur.",
     {"entities": [(17, 71, 'ADDRESS')]}),

    ("Card 4694855107211033 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Account linked to hig.057ij@gmail.com.",
     {"entities": [(18, 37, 'EMAIL')]}),

    ("Please ship to Plot number 4, Block, GT Rd, opposite Kalyanpur police station.",
     {"entities": [(15, 77, 'ADDRESS')]}),

    ("User registered with ld5bu_4l98@gmail.com.",
     {"entities": [(21, 41, 'EMAIL')]}),

    ("New card 6553073341017670 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Office is at 28 B, Stadium Road, Ekta Nagar, Bareilly, Uttar Pradesh 243001.",
     {"entities": [(13, 75, 'ADDRESS')]}),

    ("Statement sent to xyg5s1n5ww6mxthg4c45@gmail.com successfully.",
     {"entities": [(18, 48, 'EMAIL')]}),

    ("OTP sent to y2iq11mvk0@gmail.com.",
     {"entities": [(12, 32, 'EMAIL')]}),

    ("Account linked to byqx8f1@gmail.com.",
     {"entities": [(18, 35, 'EMAIL')]}),

    ("Bill sent to dq7lu@gmail.com for card 6588189909510065.",
     {"entities": [(13, 28, 'EMAIL'), (38, 54, 'CREDIT_CARD')]}),

    ("Email l.a2w2kev@gmail.com not verified.",
     {"entities": [(6, 25, 'EMAIL')]}),

    ("Statement sent to c59sk7biqyr8@gmail.com successfully.",
     {"entities": [(18, 40, 'EMAIL')]}),

    ("Send report to g5t7d47e@gmail.com.",
     {"entities": [(15, 33, 'EMAIL')]}),

    ("Send OTP to mtob.dm9c5fnb2h@gmail.com immediately.",
     {"entities": [(12, 37, 'EMAIL')]}),

    ("OTP sent to hipbnr4b457@gmail.com.",
     {"entities": [(12, 33, 'EMAIL')]}),

    ("Transaction on card 342415508544963 was declined.",
     {"entities": [(20, 35, 'CREDIT_CARD')]}),

    ("Office is at BIDA Niryat Bhavan, Chedibeer, Bhadohi Nagar Palika, Uttar Pradesh 221401.",
     {"entities": [(13, 86, 'ADDRESS')]}),

    ("Account linked to unxnn8f._ii@gmail.com.",
     {"entities": [(18, 39, 'EMAIL')]}),

    ("Branch office at QM4V+QJ3, Uttri Wajidpur, Khasanpur, Jaunpur, Uttar Pradesh 222001.",
     {"entities": [(17, 83, 'ADDRESS')]}),

    ("Send report to vache3@gmail.com.",
     {"entities": [(15, 31, 'EMAIL')]}),

    ("New card 5425184350676819 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Send statement to th.75so0h6aouj_ypro9@gmail.com for Neha Joshi.",
     {"entities": [(18, 48, 'EMAIL'), (53, 63, 'PERSON')]}),

    ("Pallavi Joshi used card 4883175859657043 at H-13, Zen Apartments, Green Park, New Delhi, Delhi 110016.",
     {"entities": [(0, 13, 'PERSON'), (24, 40, 'CREDIT_CARD'), (44, 101, 'ADDRESS')]}),

    ("Delivery address is Patel Garden, Block B, Delhi, 110059.",
     {"entities": [(20, 56, 'ADDRESS')]}),

    ("Send statement to z2qjooamo9meqvjc6@gmail.com for Neha Joshi.",
     {"entities": [(18, 45, 'EMAIL'), (50, 60, 'PERSON')]}),

    ("Email udctnt@gmail.com not verified.",
     {"entities": [(6, 22, 'EMAIL')]}),

    ("Notification sent to adrb0m780_6@gmail.com.",
     {"entities": [(21, 42, 'EMAIL')]}),

    ("Send report to x2yrozyl16tfddfqp@gmail.com.",
     {"entities": [(15, 42, 'EMAIL')]}),

    ("Customer Dinesh Rao lives at 1275, Prem Madan Infinity, Gwalior Rd, Civil Lines, Loha Mandi, Jhansi. Contact: fj6ft9ar@gmail.com.",
     {"entities": [(9, 19, 'PERSON'), (29, 99, 'ADDRESS'), (110, 128, 'EMAIL')]}),

    ("Office is at Omaxe, NRI City Rd, NRI City, Omega II, Greater Noida, Uttar Pradesh 201310.",
     {"entities": [(13, 88, 'ADDRESS')]}),

    ("Charge card number 4261679332905550 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("User registered with r0cmp40z7alpp@gmail.com.",
     {"entities": [(21, 44, 'EMAIL')]}),

    ("Card 5506290537249913 linked to sye4xbyd75l7vv@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 56, 'EMAIL')]}),

    ("Bill sent to lb9a814n5u.ypibdjp.0@gmail.com for card 4656783392278224.",
     {"entities": [(13, 43, 'EMAIL'), (53, 69, 'CREDIT_CARD')]}),

    ("Registered address: busa wali gali, Dam Rd, Budaun, Uttar Pradesh 243601.",
     {"entities": [(20, 72, 'ADDRESS')]}),

    ("Transaction on card 5147787718526429 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Registered address: sheetla mandir, Bathua, Riwa Rd, Mirzapur, Uttar Pradesh 231001.",
     {"entities": [(20, 83, 'ADDRESS')]}),

    ("Property located at 110 ka Jawahar nagar Mehnagar near guara inter collage, Azamgarh.",
     {"entities": [(20, 84, 'ADDRESS')]}),

    ("Card 343127745976499 was used at ATM.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Send documents to Hospital In Front, Gopal Mandir, Near, Dis, near District hospital.",
     {"entities": [(18, 84, 'ADDRESS')]}),

    ("Disputed transaction on card 379967547186737.",
     {"entities": [(29, 44, 'CREDIT_CARD')]}),

    ("Delivery address is Auraiya Phaphund Rd, Satteshwar, Tilak Nagar, Auraiya, Uttar Pradesh 206122.",
     {"entities": [(20, 95, 'ADDRESS')]}),

    ("Billing address: 22/349-350, Mayur Vihar Phase I, Part 2, Trilokpuri, New Delhi, Delhi.",
     {"entities": [(17, 86, 'ADDRESS')]}),

    ("Block card 5530888000712786 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Delivery address is Q38G+XMV, Deegha, Khalilabad, Uttar Pradesh 272175.",
     {"entities": [(20, 70, 'ADDRESS')]}),

    ("Bill sent to e2e83uk@gmail.com for card 346832024800484.",
     {"entities": [(13, 30, 'EMAIL'), (40, 55, 'CREDIT_CARD')]}),

    ("Send OTP to t65uc6mxvp@gmail.com immediately.",
     {"entities": [(12, 32, 'EMAIL')]}),

    ("Block card 4671210577824198 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Send report to toz1g4cmmzq5ysbaff@gmail.com.",
     {"entities": [(15, 43, 'EMAIL')]}),

    ("Disputed transaction on card 6549656800094905.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Invoice to be sent at W6VC+X9X, New Colony, Baghpat, Uttar Pradesh 250609.",
     {"entities": [(22, 73, 'ADDRESS')]}),

    ("Card 4407797668456808 linked to ki32zlteqjgi7l@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 56, 'EMAIL')]}),

    ("Verify card 4564366190062204 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Send OTP to vw4arnik@gmail.com immediately.",
     {"entities": [(12, 30, 'EMAIL')]}),

    ("Charge card number 4716026240732265 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Notification sent to d_6lnxmzm277g@gmail.com.",
     {"entities": [(21, 44, 'EMAIL')]}),

    ("Property located at Dilippur Road, Achalpur, Bela Pratapgarh, Uttar Pradesh 230127.",
     {"entities": [(20, 82, 'ADDRESS')]}),

    ("Please contact vga3t7h5@gmail.com for queries.",
     {"entities": [(15, 33, 'EMAIL')]}),

    ("Send OTP to k72djcey4@gmail.com immediately.",
     {"entities": [(12, 31, 'EMAIL')]}),

    ("Account linked to qyqnd@gmail.com.",
     {"entities": [(18, 33, 'EMAIL')]}),

    ("OTP sent to qz23.icy@gmail.com.",
     {"entities": [(12, 30, 'EMAIL')]}),

    ("Send statement to q0_j0_drmbxz@gmail.com for Manoj Tiwari.",
     {"entities": [(18, 40, 'EMAIL'), (45, 57, 'PERSON')]}),

    ("Send OTP to pxqeerr.0bpi2x3fbgih@gmail.com immediately.",
     {"entities": [(12, 42, 'EMAIL')]}),

    ("New card 343033894565304 issued to customer.",
     {"entities": [(9, 24, 'CREDIT_CARD')]}),

    ("Disputed transaction on card 5483005376655483.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Card 5357399293701489 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Notification sent to dr37v0e@gmail.com.",
     {"entities": [(21, 38, 'EMAIL')]}),

    ("Card 347987294621290 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Account linked to eelzqusmy506414ty4l@gmail.com.",
     {"entities": [(18, 47, 'EMAIL')]}),

    ("Suresh Patel at Plot No E, 32, Patparganj Industrial Area, Tikariya Upside, Gauriganj, email pcj5r0yd3u0lbqf_i@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 85, 'ADDRESS'), (93, 120, 'EMAIL')]}),

    ("OTP sent to shnj4okj6@gmail.com.",
     {"entities": [(12, 31, 'EMAIL')]}),

    ("Meena Patel at RPRW+6GQ, Oel, Oel Dhakwa, Uttar Pradesh 262725, email mji1xfw9wybp45._e35@gmail.com.",
     {"entities": [(0, 11, 'PERSON'), (15, 62, 'ADDRESS'), (70, 99, 'EMAIL')]}),

    ("Invoice to be sent at Rail Vihar, Medical College Road, Chargawa,, Gorakhpur.",
     {"entities": [(22, 76, 'ADDRESS')]}),

    ("Card 4781004049046637 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Rohit Mehta card 4048394397021087 blocked.",
     {"entities": [(0, 11, 'PERSON'), (17, 33, 'CREDIT_CARD')]}),

    ("Send report to l3_wo35_zcs@gmail.com.",
     {"entities": [(15, 36, 'EMAIL')]}),

    ("Rekha Iyer at Santosh Nagar, Anoopshahr Road, Bulandshahr, Uttar Pradesh 203150, email jj0.u4uo8@gmail.com.",
     {"entities": [(0, 10, 'PERSON'), (14, 79, 'ADDRESS'), (87, 106, 'EMAIL')]}),

    ("Please contact l8um9pb1es4s@gmail.com for queries.",
     {"entities": [(15, 37, 'EMAIL')]}),

    ("Send OTP to a3dg9lgiwr2qsg@gmail.com immediately.",
     {"entities": [(12, 36, 'EMAIL')]}),

    ("Send statement to qpwobeq7cvc1a45n34a@gmail.com for Geeta Rani.",
     {"entities": [(18, 47, 'EMAIL'), (52, 62, 'PERSON')]}),

    ("Shruti Desai at In front of the Prabhu Park, jhanwar, complex, Nadrai Gate Main Market Rd, email c91mgrj@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 89, 'ADDRESS'), (97, 114, 'EMAIL')]}),

    ("Transaction on card 370956526090648 was declined.",
     {"entities": [(20, 35, 'CREDIT_CARD')]}),

    ("Delivery address is Roza Road, Puttulal Chauraha Near Police Chowki Fatehpur, Shahjahanpur.",
     {"entities": [(20, 90, 'ADDRESS')]}),

    ("Please ship to HF9V+PRQ, Wajidpur Urf Rajepur, Uttar Pradesh 209801.",
     {"entities": [(15, 67, 'ADDRESS')]}),

    ("Card 5523668305334763 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Amit Kumar at WQGW+6CX, Yaduvansh Nagar, Gautam Nagar, Fatehpur, Uttar Pradesh 212601, email e7n9x7ct0ohdlx@gmail.com.",
     {"entities": [(0, 10, 'PERSON'), (14, 85, 'ADDRESS'), (93, 117, 'EMAIL')]}),

    ("Payment failed for card 5540452303162056.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Send documents to Lane Number 14, Gandhi Colony, Muzaffarnagar, Uttar Pradesh 251001.",
     {"entities": [(18, 84, 'ADDRESS')]}),

    ("Vikram Malhotra used card 6061485060450957 at Court Rd, opp. Hdfc Bank, Gill Colony, Saharanpur, Uttar Pradesh 247001.",
     {"entities": [(0, 15, 'PERSON'), (26, 42, 'CREDIT_CARD'), (46, 117, 'ADDRESS')]}),

    ("Notification sent to fkl4tbt@gmail.com.",
     {"entities": [(21, 38, 'EMAIL')]}),

    ("Send report to zmqmm8w6f8@gmail.com.",
     {"entities": [(15, 35, 'EMAIL')]}),

    ("Card 5598433505648032 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Card 5327641908801567 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Recovery email set to fzx08uuzleqzqpl_7@gmail.com.",
     {"entities": [(22, 49, 'EMAIL')]}),

    ("Verify card 4809927987932949 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Send statement to qpiv1_v3marz8t4io@gmail.com for Vikram Malhotra.",
     {"entities": [(18, 45, 'EMAIL'), (50, 65, 'PERSON')]}),

    ("Customer lives at MGR4+XM2, Hamirpur, Himachal Pradesh 177001.",
     {"entities": [(18, 61, 'ADDRESS')]}),

    ("Notification sent to rsoeiasxq0laol8kx@gmail.com.",
     {"entities": [(21, 48, 'EMAIL')]}),

    ("Card 340339737020561 was used at ATM.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Delivery address is Bhartendu Harish Chandra Marg, Arya Nagar, Karkardooma, Anand Vihar.",
     {"entities": [(20, 87, 'ADDRESS')]}),

    ("Bill sent to s0lmi7zq4_o863n6ago@gmail.com for card 5276080586247830.",
     {"entities": [(13, 42, 'EMAIL'), (52, 68, 'CREDIT_CARD')]}),

    ("Suresh Patel used card 4758606635024268 at Aurangabad, Uttar Pradesh 272175.",
     {"entities": [(0, 12, 'PERSON'), (23, 39, 'CREDIT_CARD'), (43, 75, 'ADDRESS')]}),

    ("Billing address: Saifabad, Pratapgarh, Sagra, Uttar Pradesh 230001.",
     {"entities": [(17, 66, 'ADDRESS')]}),

    ("Send report to mc8m1ed@gmail.com.",
     {"entities": [(15, 32, 'EMAIL')]}),

    ("User registered with mx.v5@gmail.com.",
     {"entities": [(21, 36, 'EMAIL')]}),

    ("Email f1fa1p8w87cnhhqay3@gmail.com not verified.",
     {"entities": [(6, 34, 'EMAIL')]}),

    ("Registered address: M7XH+274, Yamuna Vihar Vijay Park Rd, Block C, Yamuna Vihar, Shahdara.",
     {"entities": [(20, 89, 'ADDRESS')]}),

    ("Send documents to CH7G+366, Surya Bhan Singh Rd, Dhaurahra, Uttar Pradesh 221409.",
     {"entities": [(18, 80, 'ADDRESS')]}),

    ("Email gflvh1zto@gmail.com not verified.",
     {"entities": [(6, 25, 'EMAIL')]}),

    ("Delivery address is 737F+FP, Civil Line, Sultanpur, Uttar Pradesh 228001.",
     {"entities": [(20, 72, 'ADDRESS')]}),

    ("Property located at LIC BLDG, Ansari Rd, Muzaffarnagar, Uttar Pradesh 251001.",
     {"entities": [(20, 76, 'ADDRESS')]}),

    ("Invoice to be sent at VXQ5+X4P, Badanpur, Uttar Pradesh 230002.",
     {"entities": [(22, 62, 'ADDRESS')]}),

    ("Notification sent to ievz53qgp5pqqj13yo@gmail.com.",
     {"entities": [(21, 49, 'EMAIL')]}),

    ("Billing address: Garh Rd, near Pantaloons, Mangal Pandey Nagar, Ramgarhi, Meerut.",
     {"entities": [(17, 80, 'ADDRESS')]}),

    ("Property located at Padma Tower, 33/1, Garh Rd, opposite BSNL, Sector 3, Shastri Nagar, Meerut.",
     {"entities": [(20, 94, 'ADDRESS')]}),

    ("Card 343567122187293 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Customer lives at Phase 2, B-4 shradha puri, Service road, near kailashi hospital.",
     {"entities": [(18, 81, 'ADDRESS')]}),

    ("Send report to bvynm4c1vge7g_zh@gmail.com.",
     {"entities": [(15, 41, 'EMAIL')]}),

    ("Registered address: 2P75+3CR, Sofipur, Meerut, Uttar Pradesh 250001.",
     {"entities": [(20, 67, 'ADDRESS')]}),

    ("Card 4837303220488488 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Billing address: F2CX+XP5, Katra, Shravasti, Mahdeiya, Uttar Pradesh 271805.",
     {"entities": [(17, 75, 'ADDRESS')]}),

    ("Bill sent to srkp.q6le@gmail.com for card 4195480726541288.",
     {"entities": [(13, 32, 'EMAIL'), (42, 58, 'CREDIT_CARD')]}),

    ("Office is at WRGG+HGF, Shanti Nagar, Maswani, Fatehpur, Uttar Pradesh 212601.",
     {"entities": [(13, 76, 'ADDRESS')]}),

    ("Delivery address is No E/111, Plot No 5, Lal Kuan, Ghaziabad, Uttar Pradesh 201001.",
     {"entities": [(20, 82, 'ADDRESS')]}),

    ("Charge card number 6096434866819309 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Property located at MIET College, sarthak city, near Baghpat Road, Meerut, Uttar Pradesh 250005.",
     {"entities": [(20, 95, 'ADDRESS')]}),

    ("Send documents to first floor, Plot no. 25, Ranhola Rd, near commander chowk, Vikas Nagar.",
     {"entities": [(18, 89, 'ADDRESS')]}),

    ("Block card 5105139434749163 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Email w4l.kqlu73hj@gmail.com not verified.",
     {"entities": [(6, 28, 'EMAIL')]}),

    ("Dinesh Rao card 6051353320853263 blocked.",
     {"entities": [(0, 10, 'PERSON'), (16, 32, 'CREDIT_CARD')]}),

    ("Billing address: plot No.20, 21, Gate No. 2, Ecotech-II, Udyog Vihar, Greater Noida.",
     {"entities": [(17, 83, 'ADDRESS')]}),

    ("Recovery email set to t2dh8@gmail.com.",
     {"entities": [(22, 37, 'EMAIL')]}),

    ("Verify card 6510233012358445 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Verify card 6020319975324748 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Charge card number 347170538822828 for INR 2000.",
     {"entities": [(19, 34, 'CREDIT_CARD')]}),

    ("Transaction on card 345585022192469 was declined.",
     {"entities": [(20, 35, 'CREDIT_CARD')]}),

    ("Customer Suresh Patel lives at JG3R+F6, Alampur, Uttar Pradesh 224145. Contact: h_bz.y@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 69, 'ADDRESS'), (80, 96, 'EMAIL')]}),

    ("Invoice to be sent at Shop No.14, Ram Janambhumi, Swetambar Jain Mandir Rd, Tulsi Nagar, Ayodhya.",
     {"entities": [(22, 96, 'ADDRESS')]}),

    ("Branch office at FJ6J+HR2, Bundelkhand University, Jhansi, Uttar Pradesh 284128.",
     {"entities": [(17, 79, 'ADDRESS')]}),

    ("Send documents to Q48W+9P2, near Stadium DM Camp Office, Civil Line, Ballia.",
     {"entities": [(18, 75, 'ADDRESS')]}),

    ("Statement sent to y26l7fi1c@gmail.com successfully.",
     {"entities": [(18, 37, 'EMAIL')]}),

    ("Branch office at WQ9R+993, Joniha Rd, Jai Ram Nagar, Fatehpur, Uttar Pradesh 212601.",
     {"entities": [(17, 83, 'ADDRESS')]}),

    ("Customer Suresh Patel lives at WQWJ+X4W, Main Rd, Maharaj Nagar, Lakhimpur, Uttar Pradesh 262701. Contact: gsrd1b@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 96, 'ADDRESS'), (107, 123, 'EMAIL')]}),

    ("Block card 374876724463154 immediately.",
     {"entities": [(11, 26, 'CREDIT_CARD')]}),

    ("Registered address: Delhi Rd, Majholi, Majhola, Moradabad, Uttar Pradesh 244001.",
     {"entities": [(20, 79, 'ADDRESS')]}),

    ("Block card 5416530554975959 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Office is at Shivaji Nagar, Uttar Pradesh 272207.",
     {"entities": [(13, 48, 'ADDRESS')]}),

    ("Please contact zk6rmyrwuutwzebrjqz@gmail.com for queries.",
     {"entities": [(15, 44, 'EMAIL')]}),

    ("Tarun Khanna at Police station cyber crime, Avas Vikas, Hapur, Uttar Pradesh 245101, email jrk8k6@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 83, 'ADDRESS'), (91, 107, 'EMAIL')]}),

    ("Send OTP to gmts.b5kg@gmail.com immediately.",
     {"entities": [(12, 31, 'EMAIL')]}),

    ("Send statement to zb1fz27@gmail.com for Sanjay Gupta.",
     {"entities": [(18, 35, 'EMAIL'), (40, 52, 'PERSON')]}),

    ("Send report to y17qvrltdz3292@gmail.com.",
     {"entities": [(15, 39, 'EMAIL')]}),

    ("Transaction on card 6005256435471087 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Send documents to 4HR4+448, Ganga Darshan Colony, Saket Puri Colony, Mirzapur.",
     {"entities": [(18, 77, 'ADDRESS')]}),

    ("Send statement to cxd63wrbursl54nkznp8@gmail.com for Rohit Mehta.",
     {"entities": [(18, 48, 'EMAIL'), (53, 64, 'PERSON')]}),

    ("Statement sent to bvvzz904sivsf1@gmail.com successfully.",
     {"entities": [(18, 42, 'EMAIL')]}),

    ("Shruti Desai card 5399045861476515 blocked.",
     {"entities": [(0, 12, 'PERSON'), (18, 34, 'CREDIT_CARD')]}),

    ("Disputed transaction on card 6086823130747344.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Sanjay Gupta used card 6553274035142580 at Salek chand vihar, near City Green Resort, Shamli, Uttar Pradesh 247776.",
     {"entities": [(0, 12, 'PERSON'), (23, 39, 'CREDIT_CARD'), (43, 114, 'ADDRESS')]}),

    ("Send statement to c_wkl5955amenxr@gmail.com for Sanjay Gupta.",
     {"entities": [(18, 43, 'EMAIL'), (48, 60, 'PERSON')]}),

    ("Send OTP to qasei78fldyu_x@gmail.com immediately.",
     {"entities": [(12, 36, 'EMAIL')]}),

    ("Notification sent to b_uthm@gmail.com.",
     {"entities": [(21, 37, 'EMAIL')]}),

    ("Disputed transaction on card 349466447829131.",
     {"entities": [(29, 44, 'CREDIT_CARD')]}),

    ("Invoice to be sent at House no. 71, Block I, I-Block, Govindpuram, Ghaziabad.",
     {"entities": [(22, 76, 'ADDRESS')]}),

    ("Card 376841413236442 linked to this account.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Invoice to be sent at HDFC Bank Ltd Eye Hospital, Road, Sitapur, Uttar Pradesh 261001.",
     {"entities": [(22, 85, 'ADDRESS')]}),

    ("Tarun Khanna at 2272 basement hudson line kingsway camp GTB Nagar, 17, email rewl3ce9qno@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 69, 'ADDRESS'), (77, 98, 'EMAIL')]}),

    ("Customer lives at A, 19, Main 100 Feet Rd, West Jyoti Nagar, Durgapuri Extension.",
     {"entities": [(18, 80, 'ADDRESS')]}),

    ("Invoice to be sent at Khalapar, Muzaffarnagar, NH-58, Meerut Road, Muzaffarnagar, Muzaffarnagar.",
     {"entities": [(22, 95, 'ADDRESS')]}),

    ("Send OTP to ng9afv@gmail.com immediately.",
     {"entities": [(12, 28, 'EMAIL')]}),

    ("Verify card 6067264731821304 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Payment failed for card 341822761813007.",
     {"entities": [(24, 39, 'CREDIT_CARD')]}),

    ("Card 6503899292919967 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Office is at 1st Floor, Khasra No. 52 No, 46-A, near Chara Mandi, Roshan Mandi.",
     {"entities": [(13, 78, 'ADDRESS')]}),

    ("Charge card number 378687981338984 for INR 2000.",
     {"entities": [(19, 34, 'CREDIT_CARD')]}),

    ("Office is at Raja Pratap Bahadur Park, Uttar Pradesh 230001.",
     {"entities": [(13, 59, 'ADDRESS')]}),

    ("OTP sent to mjzmt1f5dtdt5j5b5jg@gmail.com.",
     {"entities": [(12, 41, 'EMAIL')]}),

    ("Charge card number 4744539682440395 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Sunita Verma used card 6528619703527982 at Civil Lines, Bareilly, Uttar Pradesh 243001.",
     {"entities": [(0, 12, 'PERSON'), (23, 39, 'CREDIT_CARD'), (43, 86, 'ADDRESS')]}),

]

VAL_DATA = [
    ("Invoice to be sent at Plot No B-319, Pocket B, Phase -I, Okhla Industrial Estate, New Delhi.",
     {"entities": [(22, 91, 'ADDRESS')]}),

    ("Invoice to be sent at 37X7+X8P, Baraut, Uttar Pradesh 250611.",
     {"entities": [(22, 60, 'ADDRESS')]}),

    ("Notification sent to dubcosnduwc1@gmail.com.",
     {"entities": [(21, 43, 'EMAIL')]}),

    ("Property located at 58/54, Ash Bhairo, Govindpura, Varanasi, Uttar Pradesh 221001.",
     {"entities": [(20, 81, 'ADDRESS')]}),

    ("Sunita Verma at Ground Floor, Konark Building, opposite Vijay sales, RDC, Block 1, email dz2qh8@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 81, 'ADDRESS'), (89, 105, 'EMAIL')]}),

    ("Invoice to be sent at F867+VP3, Shamli, Uttar Pradesh 247776.",
     {"entities": [(22, 60, 'ADDRESS')]}),

    ("Card 6069217924228441 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("New card 343009214340734 issued to customer.",
     {"entities": [(9, 24, 'CREDIT_CARD')]}),

    ("Nisha Agarwal used card 349671876882674 at PQJP+MF8, Swarg Ashram Rd, Shankar Ganj, Bhagwanpuri, kavi Nagar, Hapur.",
     {"entities": [(0, 13, 'PERSON'), (24, 39, 'CREDIT_CARD'), (43, 114, 'ADDRESS')]}),

    ("Transaction on card 376328047352886 was declined.",
     {"entities": [(20, 35, 'CREDIT_CARD')]}),

    ("Customer lives at Pocket B-6, Pocket 6, Sector 4, Rohini, Delhi, 110085.",
     {"entities": [(18, 71, 'ADDRESS')]}),

    ("Delivery address is CVFG+76M, Arail, Prayagraj, Uttar Pradesh 211008.",
     {"entities": [(20, 68, 'ADDRESS')]}),

    ("Card 6552923541088537 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Charge card number 6028480331674486 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Please ship to RQC8+4HC, DAFALI TOLA, PURANI, Basti, Uttar Pradesh.",
     {"entities": [(15, 66, 'ADDRESS')]}),

    ("Card 4003770161323140 linked to sdscktt32ag@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 53, 'EMAIL')]}),

    ("Please ship to Mashal talkies, Main Rd, Chedibeer, Bhadohi Nagar Palika, Piyari.",
     {"entities": [(15, 79, 'ADDRESS')]}),

    ("OTP sent to kt75g@gmail.com.",
     {"entities": [(12, 27, 'EMAIL')]}),

    ("Charge card number 4387510773837935 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("OTP sent to vlkq7p5ryp2c6nvz@gmail.com.",
     {"entities": [(12, 38, 'EMAIL')]}),

    ("Payment failed for card 5195068364300513.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Block card 372298741715153 immediately.",
     {"entities": [(11, 26, 'CREDIT_CARD')]}),

    ("Account linked to hnyqa769p8vxq7_lg@gmail.com.",
     {"entities": [(18, 45, 'EMAIL')]}),

    ("Please ship to R22M+989, Chah Khazan Khan, Pacca Baagh, Rampur, Uttar Pradesh 244901.",
     {"entities": [(15, 84, 'ADDRESS')]}),

    ("Office is at H9XG+Q4M, Govindpur Goriyon Rd, Govindpur Goriyon, Uttar Pradesh 212217.",
     {"entities": [(13, 84, 'ADDRESS')]}),

    ("Notification sent to e5rb14@gmail.com.",
     {"entities": [(21, 37, 'EMAIL')]}),

    ("Account linked to ua5geq0ie3vo@gmail.com.",
     {"entities": [(18, 40, 'EMAIL')]}),

    ("Bill sent to nhff0wwsg.geqmcc5bd@gmail.com for card 4216128215480736.",
     {"entities": [(13, 42, 'EMAIL'), (52, 68, 'CREDIT_CARD')]}),

    ("Transaction on card 341304786919613 was declined.",
     {"entities": [(20, 35, 'CREDIT_CARD')]}),

    ("Statement sent to k9nr4cf@gmail.com successfully.",
     {"entities": [(18, 35, 'EMAIL')]}),

    ("Card 4113675840480399 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Billing address: 35GG+HXQ, Rahul Sanskrityayan Rd, Azamatpur Kodur, Azamgarh.",
     {"entities": [(17, 76, 'ADDRESS')]}),

    ("Charge card number 5497708206047155 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Billing address: H6RM+5WQ, CGO Complex, Pragati Vihar, New Delhi, Delhi 110003.",
     {"entities": [(17, 78, 'ADDRESS')]}),

    ("Notification sent to cehqznvoocjw93xe698@gmail.com.",
     {"entities": [(21, 50, 'EMAIL')]}),

    ("New card 5129532149348744 issued to customer.",
     {"entities": [(9, 25, 'CREDIT_CARD')]}),

    ("Bill sent to z9c86vewk98f1z@gmail.com for card 6052022923714316.",
     {"entities": [(13, 37, 'EMAIL'), (47, 63, 'CREDIT_CARD')]}),

    ("Charge card number 4318826722515378 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Office is at Karari, Uttar Pradesh 212206.",
     {"entities": [(13, 41, 'ADDRESS')]}),

    ("Card 345342596454372 reported stolen.",
     {"entities": [(5, 20, 'CREDIT_CARD')]}),

    ("Card 4595039533501407 linked to c0suib6mv.a757x@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 57, 'EMAIL')]}),

    ("Notification sent to skno7l@gmail.com.",
     {"entities": [(21, 37, 'EMAIL')]}),

    ("Please ship to NH 56, Lucknow - Sultanpur Rd, Amhat, Sultanpur, Uttar Pradesh 228001.",
     {"entities": [(15, 84, 'ADDRESS')]}),

    ("Customer Suresh Patel lives at FFCX+XWP, Barmupur, Kasba Auraiya, Auraiya, Uttar Pradesh 206122. Contact: p_695us76wgfrda48@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 95, 'ADDRESS'), (106, 133, 'EMAIL')]}),

    ("Disputed transaction on card 6042742203241599.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Property located at W369+WGF, Badar Bagh, Aligarh, Uttar Pradesh 202001.",
     {"entities": [(20, 71, 'ADDRESS')]}),

    ("Card 4138139551647214 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Send statement to vddohzhci6@gmail.com for Vikram Malhotra.",
     {"entities": [(18, 38, 'EMAIL'), (43, 58, 'PERSON')]}),

    ("OTP sent to o_dczqla1ou.m@gmail.com.",
     {"entities": [(12, 35, 'EMAIL')]}),

    ("OTP sent to iccred13@gmail.com.",
     {"entities": [(12, 30, 'EMAIL')]}),

    ("Ramesh Babu at Agra Rd, Devpura, DIST, Mainpuri, Uttar Pradesh 205001, email ej0mad@gmail.com.",
     {"entities": [(0, 11, 'PERSON'), (15, 69, 'ADDRESS'), (77, 93, 'EMAIL')]}),

    ("Send statement to c1qlnh78bjkvclecsk@gmail.com for Deepika Nair.",
     {"entities": [(18, 46, 'EMAIL'), (51, 63, 'PERSON')]}),

    ("Disputed transaction on card 4550828107599215.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Billing address: 92H6+MQJ, Barah, Uttar Pradesh 209311.",
     {"entities": [(17, 54, 'ADDRESS')]}),

    ("User registered with w.szrymkbu728@gmail.com.",
     {"entities": [(21, 44, 'EMAIL')]}),

    ("Invoice to be sent at M5FJ+RC3, Back St, Block B, Shastri Nagar, Delhi, 110052.",
     {"entities": [(22, 78, 'ADDRESS')]}),

    ("Card 5304013237633794 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Send documents to G 20, Panchsheel Garden, Navin Shahdara, Shahdara, Delhi, 110032.",
     {"entities": [(18, 82, 'ADDRESS')]}),

    ("Send documents to Roadwyas bus stand, Bhadur Nagar, Maharaj Nagar, Lakhimpur.",
     {"entities": [(18, 76, 'ADDRESS')]}),

    ("Billing address: 59-B, Manduwadih Rd, Railway Colony, Mahmoorganj, Varanasi.",
     {"entities": [(17, 75, 'ADDRESS')]}),

    ("Please contact ksikcus62l.hl6m@gmail.com for queries.",
     {"entities": [(15, 40, 'EMAIL')]}),

    ("Customer Geeta Rani lives at 2nd Floor, BIDA Niryat Bhavan, Station, near Bhadohi, Chedibeer. Contact: evrvo6aayt@gmail.com.",
     {"entities": [(9, 19, 'PERSON'), (29, 92, 'ADDRESS'), (103, 123, 'EMAIL')]}),

    ("Send OTP to v62g04zieebs7z@gmail.com immediately.",
     {"entities": [(12, 36, 'EMAIL')]}),

    ("Block card 345486935220236 immediately.",
     {"entities": [(11, 26, 'CREDIT_CARD')]}),

    ("Card 6573874432469132 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Send statement to b41afwhdzdpk67f3ey9@gmail.com for Ananya Krishnamurthy.",
     {"entities": [(18, 47, 'EMAIL'), (52, 72, 'PERSON')]}),

    ("Property located at X633+QRC Anurag, Somaiya Nagar, bahadurpurUttar, Barabanki.",
     {"entities": [(20, 78, 'ADDRESS')]}),

    ("Disputed transaction on card 370977203036591.",
     {"entities": [(29, 44, 'CREDIT_CARD')]}),

    ("Send OTP to d_ckmuu2ym_jnf_u13m@gmail.com immediately.",
     {"entities": [(12, 41, 'EMAIL')]}),

    ("Transaction on card 6019334719317910 was declined.",
     {"entities": [(20, 36, 'CREDIT_CARD')]}),

    ("Billing address: Shriji Market, Kadamb Vihar, Ronchi Bangar, Mathura, Uttar Pradesh 281006.",
     {"entities": [(17, 90, 'ADDRESS')]}),

    ("Office is at No 192, Gas Ka Chauraha, Nakhasa, Desh Nager, Bhanpur, Pilibhit.",
     {"entities": [(13, 76, 'ADDRESS')]}),

    ("Verify card 378606427317166 with bank.",
     {"entities": [(12, 27, 'CREDIT_CARD')]}),

    ("Invoice to be sent at Prem Ganj, Sipri Bazar, Jhansi, Uttar Pradesh 284003.",
     {"entities": [(22, 74, 'ADDRESS')]}),

    ("Notification sent to shz11h7@gmail.com.",
     {"entities": [(21, 38, 'EMAIL')]}),

    ("Geeta Rani used card 5179776114584191 at Awadh Kunj jamlapur, lotan imli, Barbarahana, Chak Faiz, Ghazipur.",
     {"entities": [(0, 10, 'PERSON'), (21, 37, 'CREDIT_CARD'), (41, 106, 'ADDRESS')]}),

    ("OTP sent to wly08i@gmail.com.",
     {"entities": [(12, 28, 'EMAIL')]}),

    ("Verify card 4797424154187083 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Customer lives at GSVM मेडिकल कॉलेज, Gutaiya, Rawat Pur, Kanpur, Uttar Pradesh 208002.",
     {"entities": [(18, 85, 'ADDRESS')]}),

    ("Charge card number 4254907674467149 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Customer lives at Ground Floor, Plot No-55, D Block, Shyam Nagar, Kanpur.",
     {"entities": [(18, 72, 'ADDRESS')]}),

    ("Card 6017213196393410 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Office is at WQR8+H77, LRP Rd, near siyaram marriage lawn, chauchh, chauraha.",
     {"entities": [(13, 76, 'ADDRESS')]}),

    ("Email urbw.6gp@gmail.com not verified.",
     {"entities": [(6, 24, 'EMAIL')]}),

    ("Amit Kumar at M9C6+CGJ, Link Rd, PIR Colony, Sahibabad Industrial Area Site 4, Sahibabad, email fz7x2gocjoh@gmail.com.",
     {"entities": [(0, 10, 'PERSON'), (14, 88, 'ADDRESS'), (96, 117, 'EMAIL')]}),

    ("Recovery email set to q6_wley_1ldc@gmail.com.",
     {"entities": [(22, 44, 'EMAIL')]}),

    ("Registered address: VW56+Q4X, Ghantaghar Rd, Sahar Khas Dakhini, Shahjahanpur.",
     {"entities": [(20, 77, 'ADDRESS')]}),

    ("Bill sent to jpz.tg9gmkwyptgjp9@gmail.com for card 379179592951782.",
     {"entities": [(13, 41, 'EMAIL'), (51, 66, 'CREDIT_CARD')]}),

    ("Pallavi Joshi used card 4425855133118304 at Gokuldham, Garh Rd, Gokalpur Village, Uttar Pradesh 250004.",
     {"entities": [(0, 13, 'PERSON'), (24, 40, 'CREDIT_CARD'), (44, 102, 'ADDRESS')]}),

    ("Disputed transaction on card 5323132999529421.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Customer Rahul Sharma lives at HJM6+588, Bakshi Pura, Bahraich, Uttar Pradesh 271801. Contact: we9ipzano3ugm._zpk8@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 84, 'ADDRESS'), (95, 124, 'EMAIL')]}),

    ("Registered address: MCVF+CJ8, Jhansi - Lalitpur Rd, Subhash Pura, Lalitpur.",
     {"entities": [(20, 74, 'ADDRESS')]}),

    ("Suresh Patel used card 4444118662506025 at Shivapuram Colony, Rampur, Uttar Pradesh 244901.",
     {"entities": [(0, 12, 'PERSON'), (23, 39, 'CREDIT_CARD'), (43, 90, 'ADDRESS')]}),

    ("Send OTP to w.md6143@gmail.com immediately.",
     {"entities": [(12, 30, 'EMAIL')]}),

    ("Charge card number 4760510583037212 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Rahul Sharma used card 373251493361662 at 466/A, behind Sumitra Montessori School, Vijay Laxmi Nagar, Sitapur.",
     {"entities": [(0, 12, 'PERSON'), (23, 38, 'CREDIT_CARD'), (42, 109, 'ADDRESS')]}),

    ("Send documents to 6A Sector-40/41 Ecotech-1, Greater Noida, Uttar Pradesh 201310.",
     {"entities": [(18, 80, 'ADDRESS')]}),

    ("Registered address: Natawa, Maharajganj, Uttar Pradesh 273303.",
     {"entities": [(20, 61, 'ADDRESS')]}),

    ("Card 6095868990597772 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Card 6532053214399040 linked to zsf8_uu84rbcmvaja8d@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 61, 'EMAIL')]}),

    ("Payment failed for card 5491252898395391.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Please ship to Kishni Rd, Karhal, Kirthua, Uttar Pradesh 205264.",
     {"entities": [(15, 63, 'ADDRESS')]}),

    ("Property located at Rajabari, Pariya Tal, Uttar Pradesh 273305.",
     {"entities": [(20, 62, 'ADDRESS')]}),

    ("Rohit Mehta card 5122673061161319 blocked.",
     {"entities": [(0, 11, 'PERSON'), (17, 33, 'CREDIT_CARD')]}),

    ("Property located at 35GR+HQP, Mahtab Road, Purai Ghulami, Azamgarh, Uttar Pradesh 276001.",
     {"entities": [(20, 88, 'ADDRESS')]}),

    ("Registered address: Ganga Darshan Colony, Saket Puri Colony, Mirzapur-cum-Vindhyachal.",
     {"entities": [(20, 85, 'ADDRESS')]}),

    ("Send statement to y2cxp@gmail.com for Geeta Rani.",
     {"entities": [(18, 33, 'EMAIL'), (38, 48, 'PERSON')]}),

    ("Card 370234978753211 linked to rva7w5u9zw2r@gmail.com.",
     {"entities": [(5, 20, 'CREDIT_CARD'), (31, 53, 'EMAIL')]}),

    ("Property located at Q45W+8H5, Patel Nagar, Durgapuri Colony, Naka, Faizabad.",
     {"entities": [(20, 75, 'ADDRESS')]}),

    ("Customer Amit Kumar lives at NTI College Play Ground, Lodhipur, Shahjahanpur, Uttar Pradesh 242306. Contact: fstkbe@gmail.com.",
     {"entities": [(9, 19, 'PERSON'), (29, 98, 'ADDRESS'), (109, 125, 'EMAIL')]}),

    ("Send OTP to x7x8fgc@gmail.com immediately.",
     {"entities": [(12, 29, 'EMAIL')]}),

    ("Send statement to ewidypwc.k.4ve6@gmail.com for Deepika Nair.",
     {"entities": [(18, 43, 'EMAIL'), (48, 60, 'PERSON')]}),

    ("Send OTP to zd8y2esgy3r2@gmail.com immediately.",
     {"entities": [(12, 34, 'EMAIL')]}),

    ("User registered with xke_toa63xk4v@gmail.com.",
     {"entities": [(21, 44, 'EMAIL')]}),

    ("Registered address: Plot no.-02, Rajiv Nagar, Begampur, Sector 22, Rohini, Delhi, 110086.",
     {"entities": [(20, 88, 'ADDRESS')]}),

    ("Block card 347674893219798 immediately.",
     {"entities": [(11, 26, 'CREDIT_CARD')]}),

    ("Invoice to be sent at 7788+P58, Danpur, Chandauli, Uttar Pradesh 232104.",
     {"entities": [(22, 71, 'ADDRESS')]}),

    ("Neha Joshi used card 4059839874113332 at 9HV9+2G6, Varanasi - Bhadohi Rd, Chedibeer, Bhadohi Nagar Palika.",
     {"entities": [(0, 10, 'PERSON'), (21, 37, 'CREDIT_CARD'), (41, 105, 'ADDRESS')]}),

    ("Customer lives at Medical college gate no 3 Opposid, near sheela jain hospital, Jhansi.",
     {"entities": [(18, 86, 'ADDRESS')]}),

    ("Bill sent to t4.1fkg@gmail.com for card 4491842793871236.",
     {"entities": [(13, 30, 'EMAIL'), (40, 56, 'CREDIT_CARD')]}),

    ("Billing address: VW4J+CCM, Raja Nawab Ali Marg, Kaiser Bagh, Lucknow, Uttar Pradesh 226001.",
     {"entities": [(17, 90, 'ADDRESS')]}),

    ("Send OTP to yjke36a0052t6e6@gmail.com immediately.",
     {"entities": [(12, 37, 'EMAIL')]}),

    ("OTP sent to r0643.poksa@gmail.com.",
     {"entities": [(12, 33, 'EMAIL')]}),

    ("Block card 4360465835006825 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Billing address: M. No, 90, Ring Rd, Narendra Nagar, Lok Nagar, Unnao, Uttar Pradesh 209801.",
     {"entities": [(17, 91, 'ADDRESS')]}),

    ("Billing address: MOGHBS, Mughalsarai, Chandauli, Uttar Pradesh 232101.",
     {"entities": [(17, 69, 'ADDRESS')]}),

    ("Please ship to Chowk Station Rd, near union bank, Amarjai, Verma Chauraha, Fatehpur.",
     {"entities": [(15, 83, 'ADDRESS')]}),

    ("Send documents to No.6, Old, Gali Number 1, Ashok Nagar, Gandhi Nagar, Etawah.",
     {"entities": [(18, 77, 'ADDRESS')]}),

    ("Charge card number 374524527829702 for INR 2000.",
     {"entities": [(19, 34, 'CREDIT_CARD')]}),

    ("Charge card number 4449721691849461 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Registered address: SHRI CHANDI MANDIR, Chandi Rd, Kissanganj, Hapur, Uttar Pradesh 245101.",
     {"entities": [(20, 90, 'ADDRESS')]}),

    ("Recovery email set to yd611yd.87g@gmail.com.",
     {"entities": [(22, 43, 'EMAIL')]}),

    ("Delivery address is C42H+HM8, Pihani Road, Abdul Purwa, near Police Chouki.",
     {"entities": [(20, 74, 'ADDRESS')]}),

    ("Verify card 5411552062648446 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Bill sent to z1i6gwek0@gmail.com for card 4072369837928787.",
     {"entities": [(13, 32, 'EMAIL'), (42, 58, 'CREDIT_CARD')]}),

    ("Rekha Iyer at WH47+R4C, Saraylakhanshi, Mau, NH-29, Ghazipur Mau Road, Mau, Mau, email cep8t5auz.77@gmail.com.",
     {"entities": [(0, 10, 'PERSON'), (14, 79, 'ADDRESS'), (87, 109, 'EMAIL')]}),

    ("Invoice to be sent at Mayur Vihar Phase I, Mayur Vihar, Delhi, 110091.",
     {"entities": [(22, 69, 'ADDRESS')]}),

    ("Office is at Gautam Buddha, Shop 7,8,9,Jagat Farm , Sector,Gamma Sector-I Greater Noida.",
     {"entities": [(13, 87, 'ADDRESS')]}),

    ("Customer Manoj Tiwari lives at Q2V4+262, Golf City, Bagiamau, Lucknow, Uttar Pradesh 226002. Contact: l80k9yo@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 91, 'ADDRESS'), (102, 119, 'EMAIL')]}),

    ("Disputed transaction on card 5443053499095029.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Bill sent to tht2.ab9e2bixf1@gmail.com for card 4920523718105120.",
     {"entities": [(13, 38, 'EMAIL'), (48, 64, 'CREDIT_CARD')]}),

    ("Notification sent to n_wl6m3p4kb@gmail.com.",
     {"entities": [(21, 42, 'EMAIL')]}),

    ("Charge card number 340175667693157 for INR 2000.",
     {"entities": [(19, 34, 'CREDIT_CARD')]}),

    ("Statement sent to zirdzs0kj@gmail.com successfully.",
     {"entities": [(18, 37, 'EMAIL')]}),

    ("Statement sent to e7d_sb55q_u88rtyeeyi@gmail.com successfully.",
     {"entities": [(18, 48, 'EMAIL')]}),

    ("Card 5480919298370145 was used at ATM.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Send statement to szjk_jlp9jx0oun49k@gmail.com for Pallavi Joshi.",
     {"entities": [(18, 46, 'EMAIL'), (51, 64, 'PERSON')]}),

    ("Customer lives at M6V3+93Q, F Block Vijay Nagar, Block H, Vijay Nagar, Delhi, 110009.",
     {"entities": [(18, 84, 'ADDRESS')]}),

    ("Charge card number 4442339640473688 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Email jfdeiehlv38485@gmail.com not verified.",
     {"entities": [(6, 30, 'EMAIL')]}),

    ("Payment failed for card 374983971781913.",
     {"entities": [(24, 39, 'CREDIT_CARD')]}),

    ("Please contact z6hpe@gmail.com for queries.",
     {"entities": [(15, 30, 'EMAIL')]}),

    ("User registered with sxrqwfi0w1928@gmail.com.",
     {"entities": [(21, 44, 'EMAIL')]}),

    ("Registered address: Bus Stop, Near, Sahawar Rd, Amapur, Kasganj, Uttar Pradesh 207123.",
     {"entities": [(20, 85, 'ADDRESS')]}),

    ("Customer lives at 157, Prabhat Nagar, near LIC, Saket, Meerut, Uttar Pradesh 250001.",
     {"entities": [(18, 83, 'ADDRESS')]}),

    ("Verify card 347953832257101 with bank.",
     {"entities": [(12, 27, 'CREDIT_CARD')]}),

    ("Card 373090706751913 linked to f03dfdieo9fdkxbqa@gmail.com.",
     {"entities": [(5, 20, 'CREDIT_CARD'), (31, 58, 'EMAIL')]}),

    ("Verify card 4742629066328954 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Statement sent to s1rgz@gmail.com successfully.",
     {"entities": [(18, 33, 'EMAIL')]}),

    ("Branch office at VILL: P.O. KHUNIYANV, DIST. SIDDHARTHANAGAR, Uttar Pradesh 272192.",
     {"entities": [(17, 82, 'ADDRESS')]}),

    ("Send statement to st3hb@gmail.com for Rohit Mehta.",
     {"entities": [(18, 33, 'EMAIL'), (38, 49, 'PERSON')]}),

    ("Customer lives at Ground Floor, Virat Aishwarya Complex, Sigra - Mahmoorganj Rd, Mahmoorganj.",
     {"entities": [(18, 92, 'ADDRESS')]}),

    ("Please contact e1g1kr.zs99isy6zwt1@gmail.com for queries.",
     {"entities": [(15, 44, 'EMAIL')]}),

    ("Notification sent to up6euqdmtb_ajdp@gmail.com.",
     {"entities": [(21, 46, 'EMAIL')]}),

    ("Charge card number 5483605212562353 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Account linked to f3576p@gmail.com.",
     {"entities": [(18, 34, 'EMAIL')]}),

    ("Delivery address is Q9PF+J8M, Ramjanki Nagar, Gorakhpur, Uttar Pradesh 273004.",
     {"entities": [(20, 77, 'ADDRESS')]}),

    ("Send statement to uh731ywmwnf6t@gmail.com for Sanjay Gupta.",
     {"entities": [(18, 41, 'EMAIL'), (46, 58, 'PERSON')]}),

    ("Payment failed for card 6068722406789681.",
     {"entities": [(24, 40, 'CREDIT_CARD')]}),

    ("Notification sent to o87kwxckle07fdyh@gmail.com.",
     {"entities": [(21, 47, 'EMAIL')]}),

    ("Billing address: Joshiyapura, near V mart, Bakshi Pura, Bahraich, Uttar Pradesh 271801.",
     {"entities": [(17, 86, 'ADDRESS')]}),

    ("Card 4417189421764041 linked to greh6lxgr8zqbj@gmail.com.",
     {"entities": [(5, 21, 'CREDIT_CARD'), (32, 56, 'EMAIL')]}),

    ("Verify card 373377286965650 with bank.",
     {"entities": [(12, 27, 'CREDIT_CARD')]}),

    ("Please ship to C8W7+678, Mill Rd, Shamli, Uttar Pradesh 247776.",
     {"entities": [(15, 62, 'ADDRESS')]}),

    ("Card 5592703622355766 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Card 5348175096602534 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Customer lives at GFXM+WGC, SH 38, Unnao Sector, Civil Lines, Kalyani, Unnao.",
     {"entities": [(18, 76, 'ADDRESS')]}),

    ("Send report to kg78b0c3db3pk3y@gmail.com.",
     {"entities": [(15, 40, 'EMAIL')]}),

    ("Verify card 5292750132508916 with bank.",
     {"entities": [(12, 28, 'CREDIT_CARD')]}),

    ("Registered address: 18/8, E2 Block, Nehru Vihar, Chand Vihar, New Mustafabad, Delhi, 110094.",
     {"entities": [(20, 91, 'ADDRESS')]}),

    ("User registered with v_2746s@gmail.com.",
     {"entities": [(21, 38, 'EMAIL')]}),

    ("Customer Sunita Verma lives at Shamli, Uttar Pradesh 247776. Contact: ggsu8c8@gmail.com.",
     {"entities": [(9, 21, 'PERSON'), (31, 59, 'ADDRESS'), (70, 87, 'EMAIL')]}),

    ("Card 5300326736183120 linked to this account.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("Disputed transaction on card 4771717148069907.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("Charge card number 372565914025401 for INR 2000.",
     {"entities": [(19, 34, 'CREDIT_CARD')]}),

    ("Customer Ramesh Babu lives at 777/D1, Satyendra Nagar, Sahadatpura, Mau, Uttar Pradesh 275101. Contact: gq18qw09zbati@gmail.com.",
     {"entities": [(9, 20, 'PERSON'), (30, 93, 'ADDRESS'), (104, 127, 'EMAIL')]}),

    ("Billing address: HHJM+CJ5, Sambhal, Uttar Pradesh 244302.",
     {"entities": [(17, 56, 'ADDRESS')]}),

    ("Registered address: MIRZA HADIPUR, DISTT, Mau, Uttar Pradesh 275101.",
     {"entities": [(20, 67, 'ADDRESS')]}),

    ("OTP sent to sodhlsdmtqupq@gmail.com.",
     {"entities": [(12, 35, 'EMAIL')]}),

    ("Block card 4176100597192414 immediately.",
     {"entities": [(11, 27, 'CREDIT_CARD')]}),

    ("Bill sent to jz6sk@gmail.com for card 5325036617453826.",
     {"entities": [(13, 28, 'EMAIL'), (38, 54, 'CREDIT_CARD')]}),

    ("Send documents to HH8X+53W, near Panitanki Crossing, Sakha, Bahraich, Uttar Pradesh 271801.",
     {"entities": [(18, 90, 'ADDRESS')]}),

    ("OTP sent to k302k4@gmail.com.",
     {"entities": [(12, 28, 'EMAIL')]}),

    ("Notification sent to fzys9c5@gmail.com.",
     {"entities": [(21, 38, 'EMAIL')]}),

    ("Send OTP to tn_pf5tky6xe9zb@gmail.com immediately.",
     {"entities": [(12, 37, 'EMAIL')]}),

    ("OTP sent to gwso_yikl_8_nriyqt@gmail.com.",
     {"entities": [(12, 40, 'EMAIL')]}),

    ("Disputed transaction on card 5169634667075845.",
     {"entities": [(29, 45, 'CREDIT_CARD')]}),

    ("OTP sent to iy851t68sv6z@gmail.com.",
     {"entities": [(12, 34, 'EMAIL')]}),

    ("Account linked to vat26je9ibn6wjjhnp@gmail.com.",
     {"entities": [(18, 46, 'EMAIL')]}),

    ("Card 6082378552166364 reported stolen.",
     {"entities": [(5, 21, 'CREDIT_CARD')]}),

    ("User registered with jxsa5nzk@gmail.com.",
     {"entities": [(21, 39, 'EMAIL')]}),

    ("Notification sent to fovd1ha@gmail.com.",
     {"entities": [(21, 38, 'EMAIL')]}),

    ("Charge card number 4236850009414545 for INR 2000.",
     {"entities": [(19, 35, 'CREDIT_CARD')]}),

    ("Send statement to yduzv@gmail.com for Dinesh Rao.",
     {"entities": [(18, 33, 'EMAIL'), (38, 48, 'PERSON')]}),

    ("Send statement to pjsea6ys90o6zp6e6rx1@gmail.com for Neha Joshi.",
     {"entities": [(18, 48, 'EMAIL'), (53, 63, 'PERSON')]}),

    ("Suresh Patel at M4Q5+GH8, Guru Harkishan Marg, Maulana Azad Society, Pushpanjali Enclave, email y1qlztinc6jifp85nw@gmail.com.",
     {"entities": [(0, 12, 'PERSON'), (16, 88, 'ADDRESS'), (96, 124, 'EMAIL')]}),

    ("User registered with k2nf04x2yls3lvv31@gmail.com.",
     {"entities": [(21, 48, 'EMAIL')]}),

    ("Account linked to dgpu1@gmail.com.",
     {"entities": [(18, 33, 'EMAIL')]}),

    ("Registered address: XG7J+H59, Sharda Nagar, Saharanpur, Uttar Pradesh 247001.",
     {"entities": [(20, 76, 'ADDRESS')]}),

    ("Kiran Bedi used card 5318457944001468 at P4R9+VRP, Pocket 3, Sector17, Rohini, Delhi, 110089.",
     {"entities": [(0, 10, 'PERSON'), (21, 37, 'CREDIT_CARD'), (41, 92, 'ADDRESS')]}),

]