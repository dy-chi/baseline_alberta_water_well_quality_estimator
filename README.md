<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]





<h3 align="center">Lighthouse Labs Final Project Estimating Water Well Quality Using Geospatial Analysis</h3>

  <p align="center">
    Lighthouse Labs Final Project
    <br />
    <a href="https://github.com/dy-chi/baseline_alberta_water_well_quality_estimator"><strong>Explore the docs »</strong></a>
    <br />
    <br />

  </p>
</div>









<!-- ABOUT THE PROJECT -->
## About The Project



<p align="right">(<a href="#readme-top">back to top</a>)</p>

Following the steps in the notebook and running code provided in the project will enable the user to assess whether there is a high risk of a newly drilled water well exceeding either the Maximum Allowable Concentrations or the Aesthetic Objectives outlined by Health Canada for a selection of common ions found in drinking water, as well as pH and Total Dissolved Solids.

[Link to Health Canada Guidelines](https://www.canada.ca/en/health-canada/services/environmental-workplace-health/reports-publications/water-quality/guidelines-canadian-drinking-water-quality-summary-table.html)

The data is from a collection of tests from the Baseline Water Well Test Program.

[Link to Baseline Water Well Testing Data](https://open.alberta.ca/dataset/a2266224-81c8-45ff-9f39-f224b33ff18b/resource/036057ae-c320-4438-ad20-f3618c6eb5d0/download/baselinewaterwelltestingdata-mar31-2011.pdf)

The data has a known bias of necessarily being nearby coalbed methane developments. Despite the bias, there is still a wide distribution of wells across Alberta. 

**Spatial Autocorrelation**

How closely values are clustered together in a 2-D space.

Moran's I is a measure of spatial autocorrelation that ranges from:

-1 negative dispersion where the lagged values diverge from the original value.
 
0 random dispersion.

1 similar values spatially clustered together everywhere.

In previous work NLP models were used to extract whether comments indicated fair or poor quality odor. No major correlations were found either spatially or with any of the water chemistry features.

There was a strong geospatial autocorrelation for Fluoride, Total Dissolved Solids, Bicarbonate, Sodium, and Sulfate. And weak positive correlations for most other chemistry components.

Depth from ground surface was not considered due to the sparseness of the depth data and the limited range of depths drilled to.

For a given potential well location, if there are wells within the distance at which there is a strong geospatial correlation for that feature, the mean of the feature for the returned wells is calculated and a warning is issued for estimations that exceed guidelines 

**Tableau Concentration Maps**

Simple maps are included for various water chemistry varibles, including the extracted smell quality variables which did not end up showing any geospatial patterns 


**Download the Data**
pre-extracted csv files from the bbwt.db are made available here; however, data can be downloaded below

Navigate to the Data tab in [Alberta Water Wells](https://groundwater.alberta.ca/WaterWells/) and download the zip file containing bwwt.db


<!-- CONTACT -->
## Contact

Dylan Childs - - dychilds@gmail.com

Project Link: [https://github.com/dy-chi/baseline_alberta_water_well_quality_estimator](https://github.com/dy-chi/baseline_alberta_water_well_quality_estimator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>







<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/dy-chi/baseline_alberta_water_well_quality_estimator.svg?style=for-the-badge
[contributors-url]: https://github.com/dy-chi/baseline_alberta_water_well_quality_estimator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dy-chi/baseline_alberta_water_well_quality_estimator.svg?style=for-the-badge
[forks-url]: https://github.com/dy-chi/baseline_alberta_water_well_quality_estimator/network/members
[stars-shield]: https://img.shields.io/github/stars/dy-chi/baseline_alberta_water_well_quality_estimator.svg?style=for-the-badge
[stars-url]: https://github.com/dy-chi/baseline_alberta_water_well_quality_estimator/stargazers
[issues-shield]: https://img.shields.io/github/issues/dy-chi/baseline_alberta_water_well_quality_estimator.svg?style=for-the-badge
[issues-url]: https://github.com/dy-chi/baseline_alberta_water_well_quality_estimator/issues
[license-shield]: https://img.shields.io/github/license/dy-chi/baseline_alberta_water_well_quality_estimator.svg?style=for-the-badge
[license-url]: https://github.com/dy-chi/baseline_alberta_water_well_quality_estimator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: www.linkedin.com/in/dylan-childs-59371621
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 