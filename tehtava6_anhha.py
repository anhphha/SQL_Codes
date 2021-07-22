1. SELECT * FROM Tyontekijat;

https://mongoplayground.net/p/4zQpGEX9xil

db.Tyontekijat.find()


2. UPDATE Workers SET salary = 5500 WHERE id = 2;

https://mongoplayground.net/p/oc5IoP8Uofx

db.Tyontekijat.update({
  _id: 2
},
{
  "$set": {
    "palkka": 5500
  }
})


3. SELECT * FROM Tyontekijat;

https://mongoplayground.net/p/ojD9IykhTgm

db.Tyontekijat.find()


4. SELECT nimi, palkka FROM Tyontekijat WHERE yritys='Amazon';

https://mongoplayground.net/p/jciLIcMGmMi

db.Tyontekijat.find({
  "yritys": "Amazon"
},
{
  "_id": 0,
  "nimi": 1,
  "palkka": 1,
  "yritys": 1
})


5. SELECT COUNT(*) FROM Tyontekijat WHERE yritys='Google';

https://mongoplayground.net/p/lEf2uMs63T1

db.Tyontekijat.aggregate([
  {
    "$match": {
      "yritys": "Google"
    }
  },
  {
    "$count": "Tyontekijat"
  }
])


6. SELECT nimi, yritys FROM Tyontekijat WHERE palkka>6000;

https://mongoplayground.net/p/2tqk8CFTFkr

db.Tyontekijat.find({
  "palkka": {
    "$gt": 6000
  }
},
{
  "_id": 0,
  "nimi": 1,
  "yritys": 1
})

7. SELECT yritys, COUNT(*), MAX(palkka) FROM Tyontekijat GROUP BY yritys;

https://mongoplayground.net/p/YCIkF36-eiX

db.Tyontekijat.aggregate([
  {
    $group: {
      _id: "$yritys",
      maxpalkka: {
        $max: "$palkka"
      },
      count: {
        "$sum": 1
      }
    }
  },
  {
    $project: {
      _id: 0,
      count: 1,
      yritys: "$_id",
      maxpalkka: 1
    }
  }
])
