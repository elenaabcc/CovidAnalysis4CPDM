read.csv("C:\\Users\\Regin\\Documents\\GitHub\\CovidAnalysis4CPDM\\PROGETTO\\ECDC dataset iniziale.csv")

install.packages("ISOweek")
library(ISOweek)
#Convert ISO date into usable format - 2021W51 is converted into one value that represents a week
ECDC_dataset_iniziale$Date <- ISOweek::ISOweek2date(paste0(ECDC_dataset_iniziale$YearWeekISO, "-1"))
ECDC_dataset_iniziale
write.table(ECDC_dataset_iniziale, file = "ECDC dataset iniziale.csv",
            sep = "\t", row.names = F)
ECDC_dataset_iniziale

write.csv(ECDC_dataset_iniziale,"C:\\Users\\Regin\\Documents\\GitHub\\CovidAnalysis4CPDM\\ECDC dataset iniziale.csv", row.names = FALSE)
