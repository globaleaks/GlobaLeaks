<div class="col-md-10">
  <div class="row col-md-12">
    <span data-translate="" class="custom-bold">Start date</span>
    <div class="col-md-2">
      <input type="text" class="form-control custom-select" id="startDate" ng-click="openStartDatePicker()"
        ng-model="startDate" uib-datepicker-popup="{{format}}" is-open="startDatePickerOpen" />
    </div>
    &nbsp;&nbsp;<span data-translate="" class="custom-bold">End date</span>
    <div class="col-md-2">
      <input type="text" class="form-control custom-select" id="endDate" ng-click="openEndDatePicker()"
        ng-model="endDate" uib-datepicker-popup="{{format}}" is-open="endDatePickerOpen" />
    </div>
    &nbsp;&nbsp;<span data-translate="" class="custom-bold">Channel</span>
    <div class="col-md-2"><i><select class="form-control custom-select" data-ng-model="channel"
          data-ng-options="item for item in reportingChannel"></select></i></div>
  </div>
  <br>
  <hr> <br><br>
  <h3>Submission Status</h3><br>
  <table class="table table-striped" id="tipList" data-ng-init="sortKey = 'creation_date'; sortReverse=true;">
    <thead>
      <tr>
        <th></th>
        <th>
          Total Report
        </th>
        <th>
          New
        </th>
        <th>
          Opened
        </th>
        <th>
          Closed
        </th>
        <th>
          Unlabled
        </th>
        <th>
          Labeled
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td></td>
        <td>
          {{totalReports}}
        </td>
        <td>
          {{((statusCount["New"]/ totalReports)*100).toFixed(2)}}%
        </td>
        <td>
          {{((statusCount["Opened"]/ totalReports)*100).toFixed(2)}}%
        </td>
        <td>
          {{((statusCount["Closed"]/ totalReports)*100).toFixed(2)}}%
        </td>
        <td>
          {{((unlabeledCountDefault/ totalReports)*100).toFixed(2)}}%
        </td>
        <td>
          {{((labeledCountDefault/ totalReports)*100).toFixed(2)}}%
        </td>
      </tr>
    </tbody>
  </table>

  
  <!--  <div class="row">-->
  <!--    <div class="col">-->
  <!--  <h3>Total Reports: {{totalReports}}</h3>-->
  <!--  <ul>-->
  <!--    <li ng-repeat="report in reports">-->
  <!--      Report Label: {{report.label ? report.label : "unlabeled"}} - Status: {{report.submissionStatusStr}}-->
  <!--    </li>-->
  <!--  </ul>-->
  <!--    </div>-->
  <!--  </div>-->

  <br>
  <div class="row">
    <div class="col">
      <canvas width="1200" class="lineGraph" id="statusBarChart"></canvas>
    </div>
  </div>

  <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
  <!-- <div class="row">
    <div class="col">
      <h2>Submission Statuses Doughnut</h2>
      <canvas class="doughnut" id="doughnut"></canvas>
    </div>
  </div> -->
  <hr>
  <div class="row">
    <div class="col">
      <h3>Submission Labels</h3>
      <ul>
        <li ng-repeat="(label, data) in labelCounts">
          {{label}}: {{data.count}} ({{data.percentage}})
        </li>
        <li>
          unlabeled: {{unlabeledCount.count}} ({{unlabeledCount.percentage}})
        </li>
      </ul>
    </div>
  </div>
  <div class="row">
    <div class="col">
      <h3>Submission Labels LineGraph</h3>
      <canvas class="lineGraph" id="labelCountsChart"></canvas>
    </div>
  </div>
  <hr>
  <div class="row">
    <div class="col">
      <h3>Average recipient action time difference: {{averageDiffInDays}} days</h3>
    </div>
  </div>
  <hr>
  <div class="row">
    <div class="col">
      <h3>Report Count Per Month</h3>
      <ul>
        <li ng-repeat="(monthYear, count) in reportCount">
          {{monthYear}}: {{count}} reports
        </li>
      </ul>
    </div>
  </div>
  <hr>
  <div class="row">
    <div class="col">
      <h3>TOR and HTTPS Connections</h3>
      <ul>
        <li>TOR Connections: {{ torCount }} {{ torPercentage.toFixed(2) }}%</li>
        <li>HTTPS Connections: {{ httpsCount }} {{ httpsPercentage.toFixed(2) }}%</li>
      </ul>
    </div>
  </div>
  <hr>
  <div class="row">
    <div class="col">
      <h3>UnansweredTips</h3>
      <ul>
        <li>
          UnansweredTipsCount : {{unansweredTipsCount}}
        </li>
      </ul>
    </div>
  </div>
  <hr>
  <div class="row">
    <div class="col">
      <h3>Report Count Per Month LineGraph</h3>
      <canvas class="lineGraph" id="perMonthLineGraph"></canvas>
    </div>
  </div>
</div>
