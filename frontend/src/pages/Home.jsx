import React, { useState } from "react";
import axios from "axios";
import "../App.css";
import { Helmet } from "react-helmet";

function Home() {
  const [city, setCity] = useState("");
  const [date, setDate] = useState("");
  const [aqi, setAqi] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
console.log("home page loaded");
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!city || !date) {
      setError("Please fill in both city and date.");
      return;
    }

    setLoading(true);
    setError("");
    setAqi(null);

    try {
      const response = await axios.post("http://localhost:5000/predict", {
        city,
        date,
      });
      setAqi(response.data.predicted_aqi);
    } catch (err) {
      setError("Error fetching AQI. Please try again.");
    }

    setLoading(false);
  };

  return (
    <div className="page-container">
      <Helmet>
        <title>Home | AQI Predictor</title>
      </Helmet>
      <div className="container">
        <h1 className="title">🌿 AQI Prediction Web App</h1>
        <form onSubmit={handleSubmit} className="form">
          <label>
            City:
            <select value={city} onChange={(e) => setCity(e.target.value)}>
              <option value="">Select a city</option>
              <option value="Agartala">Agartala</option>
              <option value="Agra">Agra</option>
              <option value="Ahmedabad">Ahmedabad</option>
              <option value="Aizawl">Aizawl</option>
              <option value="Ajmer">Ajmer</option>
              <option value="Akola">Akola</option>
              <option value="Alwar">Alwar</option>
              <option value="Amaravati">Amaravati</option>
              <option value="Ambala">Ambala</option>
              <option value="Amravati">Amravati</option>
              <option value="Amritsar">Amritsar</option>
              <option value="Anantapur">Anantapur</option>
              <option value="Angul">Angul</option>
              <option value="Ankleshwar">Ankleshwar</option>
              <option value="Araria">Araria</option>
              <option value="Ariyalur">Ariyalur</option>
              <option value="Arrah">Arrah</option>
              <option value="Asansol">Asansol</option>
              <option value="Aurangabad">Aurangabad</option>
              <option value="Aurangabad (Bihar)">Aurangabad (Bihar)</option>
              <option value="Baddi">Baddi</option>
              <option value="Badlapur">Badlapur</option>
              <option value="Bagalkot">Bagalkot</option>
              <option value="Baghpat">Baghpat</option>
              <option value="Bahadurgarh">Bahadurgarh</option>
              <option value="Balasore">Balasore</option>
              <option value="Ballabgarh">Ballabgarh</option>
              <option value="Banswara">Banswara</option>
              <option value="Baran">Baran</option>
              <option value="Barbil">Barbil</option>
              <option value="Bareilly">Bareilly</option>
              <option value="Baripada">Baripada</option>
              <option value="Barmer">Barmer</option>
              <option value="Barrackpore">Barrackpore</option>
              <option value="Bathinda">Bathinda</option>
              <option value="Begusarai">Begusarai</option>
              <option value="Belapur">Belapur</option>
              <option value="Belgaum">Belgaum</option>
              <option value="Bengaluru">Bengaluru</option>
              <option value="Bettiah">Bettiah</option>
              <option value="Bhagalpur">Bhagalpur</option>
              <option value="Bharatpur">Bharatpur</option>
              <option value="Bhilai">Bhilai</option>
              <option value="Bhilwara">Bhilwara</option>
              <option value="Bhiwadi">Bhiwadi</option>
              <option value="Bhiwandi">Bhiwandi</option>
              <option value="Bhiwani">Bhiwani</option>
              <option value="Bhopal">Bhopal</option>
              <option value="Bhubaneswar">Bhubaneswar</option>
              <option value="Bidar">Bidar</option>
              <option value="Bihar Sharif">Bihar Sharif</option>
              <option value="Bikaner">Bikaner</option>
              <option value="Bilaspur">Bilaspur</option>
              <option value="Bileipada">Bileipada</option>
              <option value="Brajrajnagar">Brajrajnagar</option>
              <option value="Bulandshahr">Bulandshahr</option>
              <option value="Bundi">Bundi</option>
              <option value="Buxar">Buxar</option>
              <option value="Byasanagar">Byasanagar</option>
              <option value="Byrnihat">Byrnihat</option>
              <option value="Chamarajanagar">Chamarajanagar</option>
              <option value="Chandigarh">Chandigarh</option>
              <option value="Chandrapur">Chandrapur</option>
              <option value="Charkhi Dadri">Charkhi Dadri</option>
              <option value="Chengalpattu	Chennai">Chengalpattu	Chennai</option>
              <option value="Chennai">Chennai</option>
              <option value="Chhal">Chhal</option>
              <option value="Chhapra">Chhapra</option>
              <option value="Chikkaballapur">Chikkaballapur</option>
              <option value="Chikkamagaluru">Chikkamagaluru</option>
              <option value="Chittoor">Chittoor</option>
              <option value="Chittorgarh">Chittorgarh</option>
              <option value="Churu">Churu</option>
              <option value="Coimbatore">Coimbatore</option>
              <option value="Cuddalore">Cuddalore</option>
              <option value="Cuttack">Cuttack</option>
              <option value="Damoh">Damoh</option>
              <option value="Darbhanga">Darbhanga</option>
              <option value="Dausa">Dausa</option>
              <option value="Davanagere">Davanagere</option>
              <option value="Dehradun">Dehradun</option>
              <option value="Delhi">Delhi</option>
              <option value="Dewas">Dewas</option>
              <option value="Dhanbad">Dhanbad</option>
              <option value="Dharuhera">Dharuhera</option>
              <option value="Dharwad">Dharwad</option>
              <option value="Dholpur">Dholpur</option>
              <option value="Dhule">Dhule</option>
              <option value="Dindigul">Dindigul</option>
              <option value="Durgapur">Durgapur</option>
              <option value="Eloor">Eloor</option>
              <option value="Ernakulam">Ernakulam</option>
              <option value="Faridabad">Faridabad</option>
              <option value="Fatehabad">Fatehabad</option>
              <option value="Firozabad">Firozabad</option>
              <option value="Gadag">Gadag</option>
              <option value="GandhiNagar">GandhiNagar</option>
              <option value="Gangtok">Gangtok</option>
              <option value="Gaya">Gaya</option>
              <option value="Ghaziabad">Ghaziabad</option>
              <option value="Gorakhpur">Gorakhpur</option>
              <option value="Greater Noida">Greater Noida</option>
              <option value="Gummidipoondi">Gummidipoondi</option>
              <option value="Gurugram">Gurugram</option>
              <option value="Guwahati">Guwahati</option>
              <option value="GwaliorHajipur">GwaliorHajipur</option>
              <option value="Hajipur">Hajipur</option>
              <option value="Haldia">Haldia</option>
              <option value="Hanumangarh">Hanumangarh</option>
              <option value="HapurHassan">HapurHassan</option>
              <option value="Hassan">Hassan</option>
              <option value="Haveri">Haveri</option>
              <option value="Hisar">Hisar</option>
              <option value="Hosur">Hosur</option>
              <option value="Howrah">Howrah</option>
              <option value="Hubballi">Hubballi</option>
              <option value="Hyderabad">Hyderabad</option>
              <option value="Imphal">Imphal</option>
              <option value="Indore">Indore</option>
              <option value="Jabalpur">Jabalpur</option>
              <option value="Jaipur">Jaipur</option>
              <option value="Jaisalmer">Jaisalmer</option>
              <option value="Jalandhar">Jalandhar</option>
              <option value="Jalgaon">Jalgaon</option>
              <option value="Jalna">Jalna</option>
              <option value="Jalore">Jalore</option>
              <option value="Jhalawar">Jhalawar</option>
              <option value="Jhansi">Jhansi</option>
              <option value="Jharsuguda">Jharsuguda</option>
              <option value="Jhunjhunu">Jhunjhunu</option>
              <option value="Jind">Jind</option>
              <option value="Jodhpur">Jodhpur</option>
              <option value="Jorapokhar">Jorapokhar</option>
              <option value="Kadapa">Kadapa</option>
              <option value="Kaithal">Kaithal</option>
              <option value="Kalaburagi">Kalaburagi</option>
              <option value="Kalyan">Kalyan</option>
              <option value="Kanchipuram">Kanchipuram</option>
              <option value="Kannur">Kannur</option>
              <option value="Kanpur">Kanpur</option>
              <option value="Karauli">Karauli</option>
              <option value="Karnal">Karnal</option>
              <option value="Karwar">Karwar</option>
              <option value="Kashipur">Kashipur</option>
              <option value="Katihar">Katihar</option>
              <option value="Katni">Katni</option>
              <option value="Keonjhar">Keonjhar</option>
              <option value="Khanna">Khanna</option>
              <option value="Khurja">Khurja</option>
              <option value="Kishanganj">Kishanganj</option>
              <option value="Kochi">Kochi</option>
              <option value="Kohima">Kohima</option>
              <option value="Kolar">Kolar</option>
              <option value="Kolhapur">Kolhapur</option>
              <option value="Kolkata">Kolkata</option>
              <option value="Kollam">Kollam</option>
              <option value="Koppal">Koppal</option>
              <option value="Korba">Korba</option>
              <option value="Kota">Kota</option>
              <option value="Kozhikode">Kozhikode</option>
              <option value="Kunjemura">Kunjemura</option>
              <option value="Kurukshetra">Kurukshetra</option>
              <option value="Latur">Latur</option>
              <option value="Loni_Dehat">Loni_Dehat</option>
              <option value="Lucknow">Lucknow</option>
              <option value="Ludhiana">Ludhiana</option>
              <option value="Madikeri">Madikeri</option>
              <option value="Mahad">Mahad</option>
              <option value="Maihar">Maihar</option>
              <option value="Mandi Gobindgarh">Mandi Gobindgarh</option>
              <option value="Mandideep">Mandideep</option>
              <option value="Mandikhera">Mandikhera</option>
              <option value="Manesar">Manesar</option>
              <option value="Mangalore">Mangalore</option>
              <option value="Manguraha">Manguraha</option>
              <option value="Medikeri">Medikeri</option>
              <option value="Meerut">Meerut</option>
              <option value="Milupara">Milupara</option>
              <option value="Moradabad">Moradabad</option>
              <option value="Motihari">Motihari</option>
              <option value="Mumbai">Mumbai</option>
              <option value="Munger">Munger</option>
              <option value="Muzaffarnagar">Muzaffarnagar</option>
              <option value="Muzaffarpur">Muzaffarpur</option>
              <option value="Mysuru">Mysuru</option>
              <option value="Nagaon">Nagaon</option>
              <option value="Nagaur">Nagaur</option>
              <option value="Nagpur">Nagpur</option>
              <option value="Naharlagun">Naharlagun</option>
              <option value="Nalbari">Nalbari</option>
              <option value="Nanded">Nanded</option>
              <option value="Nandesari">Nandesari</option>
              <option value="Narnaul">Narnaul</option>
              <option value="Nashik">Nashik</option>
              <option value="Navi Mumbai">Navi Mumbai</option>
              <option value="Nayagarh">Nayagarh</option>
              <option value="Noida">Noida</option>
              <option value="Ooty">Ooty</option>
              <option value="Pali">Pali</option>
              <option value="Palkalaiperur">Palkalaiperur</option>
              <option value="Palwal">Palwal</option>
              <option value="Panchkula">Panchkula</option>
              <option value="Panipat">Panipat</option>
              <option value="Parbhani">Parbhani</option>
              <option value="Patiala">Patiala</option>
              <option value="Patna">Patna</option>
              <option value="Pimpri Chinchwad">Pimpri Chinchwad</option>
              <option value="Pithampur">Pithampur</option>
              <option value="Pratapgarh">Pratapgarh</option>
              <option value="Prayagraj">Prayagraj</option>
              <option value="Puducherry">Puducherry</option>
              <option value="Pune">Pune</option>
              <option value="Purnia">Purnia</option>
              <option value="Raichur">Raichur</option>
              <option value="Raipur">Raipur</option>
              <option value="Rairangpur">Rairangpur</option>
              <option value="Rajamahendravaram">Rajamahendravaram</option>
              <option value="Rajgir">Rajgir</option>
              <option value="Rajsamand">Rajsamand</option>
              <option value="Ramanagara">Ramanagara</option>
              <option value="Ramanathapuram">Ramanathapuram</option>
              <option value="Ratlam">Ratlam</option>
              <option value="Rishikesh">Rishikesh</option>
              <option value="Rohtak">Rohtak</option>
              <option value="Rourkela">Rourkela</option>
              <option value="Rupnagar">Rupnagar</option>
              <option value="Sagar">Sagar</option>
              <option value="Saharsa">Saharsa</option>
              <option value="Salem">Salem</option>
              <option value="Samastipur">Samastipur</option>
              <option value="Sangli">Sangli</option>
              <option value="Sasaram">Sasaram</option>
              <option value="Satna">Satna</option>
              <option value="Sawai Madhopur">Sawai Madhopur</option>
              <option value="ShillongShivamogga">ShillongShivamogga</option>
              <option value="Shivamogga">Shivamogga</option>
              <option value="Sikar">Sikar</option>
              <option value="Silchar">Silchar</option>
              <option value="Siliguri">Siliguri</option>
              <option value="Singrauli">Singrauli</option>
              <option value="Sirohi">Sirohi</option>
              <option value="Sirsa">Sirsa</option>
              <option value="Sivasagar">Sivasagar</option>
              <option value="Siwan">Siwan</option>
              <option value="Solapur">Solapur</option>
              <option value="Sonipat">Sonipat</option>
              <option value="Sri Ganganagar">Sri Ganganagar</option>
              <option value="Srinagar">Srinagar</option>
              <option value="Suakati">Suakati</option>
              <option value="Surat">Surat</option>
              <option value="Talcher">Talcher</option>
              <option value="Tensa">Tensa</option>
              <option value="Thane">Thane</option>
              <option value="Thiruvananthapuram">Thiruvananthapuram</option>
              <option value="Thoothukudi">Thoothukudi</option>
              <option value="Thrissur">Thrissur</option>
              <option value="Tiruchirappalli">Tiruchirappalli</option>
              <option value="Tirupati">Tirupati</option>
              <option value="Tirupur">Tirupur</option>
              <option value="Tonk">Tonk</option>
              <option value="Tumakuru">Tumakuru</option>
              <option value="Tumidih">Tumidih</option>
              <option value="Udaipur">Udaipur</option>
              <option value="Udupi">Udupi</option>
              <option value="Ujjain">Ujjain</option>
              <option value="Ulhasnagar">Ulhasnagar</option>
              <option value="Vapi">Vapi</option>
              <option value="Varanasi">Varanasi</option>
              <option value="Vatva">Vatva</option>
              <option value="Vellore">Vellore</option>
              <option value="Vijayapura">Vijayapura</option>
              <option value="Vijayawada">Vijayawada</option>
              <option value="Visakhapatnam">Visakhapatnam</option>
              <option value="Vrindavan">Vrindavan</option>
              <option value="Yadgir">Yadgir</option>
              <option value="Yamunanagar">Yamunanagar</option>
              
            </select>
          </label>

          <label>
            Date:
            <input
              type="date"
              value={date}
              onChange={(e) => setDate(e.target.value)}
            />
          </label>

          <button type="submit" disabled={loading}>
            {loading ? "Predicting..." : "Predict AQI"}
          </button>

          {error && <p className="error">{error}</p>}
        </form>

        {aqi !== null && (
          <div className="result">
            <h2>📊 Predicted AQI:</h2>
            <p>{aqi}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Home;
