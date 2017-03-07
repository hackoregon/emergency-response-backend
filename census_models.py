class CensusBlock(models.Model):
    gid = models.AutoField(primary_key=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    blkgrpce = models.CharField(max_length=1, blank=True, null=True)
    geoid = models.CharField(max_length=12, blank=True, null=True)
    namelsad = models.CharField(max_length=13, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ceblocks'

class CensusEducationalAttainment(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    total = models.IntegerField()
    no_school_completed = models.IntegerField()
    nursery_school = models.IntegerField()
    kindergarten = models.IntegerField()
    first_grade = models.IntegerField()
    second_grade = models.IntegerField()
    third_grade = models.IntegerField()
    fourth_grade = models.IntegerField()
    fifth_grade = models.IntegerField()
    sixth_grade = models.IntegerField()
    seventh_grade = models.IntegerField()
    eighth_grade = models.IntegerField()
    ninth_grade = models.IntegerField()
    tenth_grade = models.IntegerField()
    eleventh_grade = models.IntegerField()
    twelvth_grade_no_diploma = models.IntegerField()
    regular_hs_diploma = models.IntegerField()
    ged_or_alternative = models.IntegerField()
    some_college_less_than_year = models.IntegerField()
    some_college_more_than_year = models.IntegerField()
    associate_degree = models.IntegerField()
    bachelor_degree = models.IntegerField()
    master_degree = models.IntegerField()
    professional_school_degree = models.IntegerField()
    doctorate_degree = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_educational_attainment'

class CensusFoodStamps(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    total = models.IntegerField()
    hh_rec_fs = models.IntegerField()
    hh_rec_fs_omo_w_disability = models.IntegerField()
    hh_rec_fs_no_disability = models.IntegerField()
    hh_dn_rec_fs = models.IntegerField()
    hh_dn_rec_fs_omo_w_disability = models.IntegerField()
    hh_dn_rec_fs_no_disability = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_food_stamps'

class CensusHouseholdIncome(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    estimate_total = models.IntegerField()
    total_less_than_10000 = models.IntegerField()
    total_10000_to_14999 = models.IntegerField()
    total_15000_to_19999 = models.IntegerField()
    total_20000_to_24999 = models.IntegerField()
    total_25000_to_29999 = models.IntegerField()
    total_30000_to_34999 = models.IntegerField()
    total_35000_to_39999 = models.IntegerField()
    total_40000_to_44999 = models.IntegerField()
    total_45000_to_49999 = models.IntegerField()
    total_50000_to_59999 = models.IntegerField()
    total_60000_to_74999 = models.IntegerField()
    total_75000_to_99999 = models.IntegerField()
    total_100000_to_124999 = models.IntegerField()
    total_125000_to_149999 = models.IntegerField()
    total_150000_to_199999 = models.IntegerField()
    total_200000_or_more = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_household_income'

class CensusHouseholdLanguage(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    estimate_total = models.IntegerField()
    english_only = models.IntegerField()
    spanish_total = models.IntegerField()
    spanish_lesh = models.IntegerField()
    spanish_notlesh = models.IntegerField()
    other_indo_euro_total = models.IntegerField()
    other_indo_euro_lesh = models.IntegerField()
    other_indo_euro_notlesh = models.IntegerField()
    asian_pacific_island_total = models.IntegerField()
    asian_pacific_island_lesh = models.IntegerField()
    asian_pacific_island_notlesh = models.IntegerField()
    other_total = models.IntegerField()
    other_lesh = models.IntegerField()
    other_notlesh = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_household_language'


class CensusHousehold65Plus(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    totals = models.IntegerField()
    oneplus_people_65plus = models.IntegerField()
    one_or_more_people_65plus_1_person = models.IntegerField()
    oneplus_people_65plus_2plus_person = models.IntegerField()
    oneplus_people_65plus_2plus_person_family = models.IntegerField()
    oneplus_people_65plus_2plus_person_nonfamily = models.IntegerField()
    no_people_65plus = models.IntegerField()
    no_people_65plus_1_person = models.IntegerField()
    no_people_65plus_2plus_person = models.IntegerField()
    no_people_65plus_2plus_person_family = models.IntegerField()
    no_people_65plus_2plus_person_nonfamily = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_households_65plus'


class CensusHousingTenure(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    estimate_total_households = models.IntegerField()
    estimate_total_owner_occupied = models.IntegerField()
    estimate_total_renter_occupied = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_housing_tenure'


class CensusMedianHouseholdIncome(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    estimate_median_household_income = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_median_household_income'


class CensusRace(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    total = models.IntegerField()
    white_alone = models.IntegerField()
    black_alone = models.IntegerField()
    american_indian_alaska_native_alone = models.IntegerField()
    asian_alone = models.IntegerField()
    native_hawaiian_pacific_islander_alone = models.IntegerField()
    some_other_alone = models.IntegerField()
    two_or_more_races = models.IntegerField()
    two_or_more_some_other = models.IntegerField()
    two_or_more_excluding_some_other_three_or_more_races = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_race'


class CensusTotalPopulation(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    estimate_total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_total_population'



class CensusBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusBlock
        fields = '__all__'

class CensusHouseholdIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusHouseholdIncome
        fields = '__all__'

class CensusHouseholdLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusHouseholdLanguage
        fields = '__all__'

class CensusHousehold65PlusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusHousehold65Plus
        fields = '__all__'

class CensusHousingTenureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusHousingTenure
        fields = '__all__'

class CensusMedianHouseholdIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusMedianHouseholdIncome
        fields = '__all__'

class CensusRaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusRace
        fields = '__all__'

class CensusTotalPopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusTotalPopulation
        fields = '__all__'

class CensusEducationalAttainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusEducationalAttainment
        fields = '__all__'



class CensusBlockListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = CensusBlock.objects.all()
    serializer_class = CensusBlockSerializer

class CensusBlockRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = CensusBlock.objects.all()
    serializer_class = CensusBlockSerializer

class CensusEducationalListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = CensusEducationalAttainment.objects.all()
    serializer_class = CensusEducationalAttainmentSerializer

class CensusEducationalRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = CensusEducationalAttainment.objects.all()
    serializer_class = CensusEducationalAttainmentSerializer

class CensusHouseholdIncomeListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = CensusHouseholdIncome.objects.all()
    serializer_class = CensusHouseholdIncomeSerializer

class CensusHouseholdIncomeRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = CensusHouseholdIncome.objects.all()
    serializer_class = CensusHouseholdIncomeSerializer

class CensusHouseholdLanguageListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = CensusHouseholdLanguage.objects.all()
    serializer_class = CensusHouseholdLanguageSerializer

class CensusHouseholdLanguageRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = CensusHouseholdLanguage.objects.all()
    serializer_class = CensusHouseholdLanguageSerializer

class CensusHousehold65PlusListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = CensusHousehold65Plus.objects.all()
    serializer_class = CensusHousehold65PlusSerializer

class CensusHousehold65PlusRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = CensusHousehold65Plus.objects.all()
    serializer_class = CensusHousehold65PlusSerializer

class CensusHousingTenureListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = CensusHousingTenure.objects.all()
    serializer_class = CensusHousingTenureSerializer

class CensusHousingTenureRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = CensusHousingTenure.objects.all()
    serializer_class = CensusHousingTenureSerializer

class CensusMedianHouseholdIncomeListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = CensusMedianHouseholdIncome.objects.all()
    serializer_class = CensusMedianHouseholdIncomeSerializer

class CensusMedianHouseholdIncomeRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = CensusMedianHouseholdIncome.objects.all()
    serializer_class = CensusMedianHouseholdIncomeSerializer

class CensusRaceListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = CensusRace.objects.all()
    serializer_class = CensusRaceSerializer

class CensusRaceListRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = CensusRace.objects.all()
    serializer_class = CensusRaceSerializer

class CensusTotalPopulationListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = CensusTotalPopulation.objects.all()
    serializer_class = CensusTotalPopulationSerializer

class CensusTotalPopulationRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = CensusTotalPopulation.objects.all()
    serializer_class = CensusTotalPopulationSerializer
