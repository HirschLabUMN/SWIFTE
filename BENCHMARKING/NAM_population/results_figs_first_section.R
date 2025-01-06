---
title: "pairedvssingleend"
output: html_document
date: "2024-11-14"
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

## R Markdown

This is an R Markdown document. Markdown is a simple formatting syntax for authoring HTML, PDF, and MS Word documents. For more details on using R Markdown see <http://rmarkdown.rstudio.com>.

When you click the **Knit** button a document will be generated that includes both content as well as the output of any embedded R code chunks within the document. You can embed an R code chunk like this:

```{r}
# Load necessary libraries
library(ggplot2)
library(reshape2)

# Create the data frame
data <- data.frame(
  X_or_more_reads = 1:10,
  precision = c(-1.993014106, -1.520809325, -1.071059396, -1.625148716, -2.386166467, -3.653232616, -5.832060013, -6.7118096, -7.839467159, -6.816286347),
  FDR = c(1.993014106, 1.520809325, 1.071059396, 1.625148716, 2.386166467, 3.653232616, 5.832060013, 6.7118096, 7.839467159, 6.816286347),
  sensitivity = c(1.584178722, 0.4775420442, -0.007255018782, -0.2037697284, -0.2247301031, -0.1648823862, -0.1208362877, -0.06688005567, -0.035511442, -0.01322848237),
  F1 = c(0.006181547577, 0.4873792732, -0.03564002132, -0.3719706073, -0.4251522312, -0.319852272, -0.2377520976, -0.1325937917, -0.07070914003, -0.02640835994),
  POD = c(3.594598491, 0.8974482195, -0.3261809794, -0.6313374021, -0.6265317891, -0.4907732231, -0.3081599308, -0.1705992599, -0.1171368158, -0.04985823442)
)

# Reshape the data for ggplot
data_long <- melt(data, id.vars = "X_or_more_reads", variable.name = "Metric", value.name = "Value")

# Create the plot
ggplot(data_long, aes(x = X_or_more_reads, y = Value, color = Metric, group = Metric)) +
  geom_line() +
  geom_point() +
  theme_minimal() +
  labs(x = "X or More Reads",
       y = "Percent Drop",
       color = "Metric") +
  theme(legend.position = "bottom")

```
```{r}
# Load necessary libraries
library(ggplot2)
library(reshape2)

# Create the data frame
data <- data.frame(
  X_or_more_reads = 1:10,
  precision = c(-1.993014106, -1.520809325, -1.071059396, -1.625148716, -2.386166467, -3.653232616, -5.832060013, -6.7118096, -7.839467159, -6.816286347),
  FDR = c(1.993014106, 1.520809325, 1.071059396, 1.625148716, 2.386166467, 3.653232616, 5.832060013, 6.7118096, 7.839467159, 6.816286347),
  sensitivity = c(1.584178722, 0.4775420442, -0.007255018782, -0.2037697284, -0.2247301031, -0.1648823862, -0.1208362877, -0.06688005567, -0.035511442, -0.01322848237),
  F1 = c(0.006181547577, 0.4873792732, -0.03564002132, -0.3719706073, -0.4251522312, -0.319852272, -0.2377520976, -0.1325937917, -0.07070914003, -0.02640835994),
  power_of_discovery = c(3.594598491, 0.8974482195, -0.3261809794, -0.6313374021, -0.6265317891, -0.4907732231, -0.3081599308, -0.1705992599, -0.1171368158, -0.04985823442)
)

# Remove the power_of_discovery column
data <- data[, !names(data) %in% "power_of_discovery"]

# Reshape the data for ggplot
data_long <- melt(data, id.vars = "X_or_more_reads", variable.name = "Metric", value.name = "Value")

# Define your custom color palette
custom_palette <- c("#332288", "#117733", "#DDCC77", "#CC6677", "#AA4499")

# Create the plot with the custom color palette
p <- ggplot(data_long, aes(x = X_or_more_reads, y = Value, color = Metric, group = Metric)) +
  geom_line() +
  geom_point() +
  scale_color_manual(values = custom_palette) +  # Apply the custom color palette
  theme_minimal() +
  labs(x = "X or More Reads",
       y = "Percent Drop",
       color = "Metric") +
  theme(
    legend.position = "bottom",  # Place legend to the right
    legend.text = element_text(size = 8),  # Smaller font size for the legend
    legend.title = element_text(size = 10),  # Slightly larger font size for the legend title
    legend.key.size = unit(0.5, "lines"),  # Smaller legend keys
    legend.box.spacing = unit(0.5, "cm"),  # Adjust spacing between the legend and plot
    text = element_text(size = 12),  # Set font size to 12pt for all text elements
    plot.margin = margin(10, 20, 10, 10)  # Increase margin to ensure the legend fits
  ) +
  guides(color = guide_legend(nrow = 3, byrow = TRUE))  # Arrange legend in 2 rows

# Save the plot with a width of 85mm (3.35 inches) and height of 75mm (2.95 inches)
ggsave("xormore_reads_plot_no_power_of_discovery.png", plot = p, width = 85 / 25.4, height = 75 / 25.4, units = "in", dpi = 300)   # Save as 85mm width

# Optionally, you can display the plot
print(p)

```
```{r}
# Load necessary library
library(ggplot2)

# Create the data frame
data <- data.frame(
  X_or_more_reads = 1:10,
  precision = c(0.06276631791, 0.1304073255, 0.1731192611, 0.2018195321, 0.2173913043, 0.2220385675, 
                0.2202664129, 0.2124789207, 0.1940298507, 0.1485411141),
  FDR = c(0.9372336821, 0.8695926745, 0.8268807389, 0.7981804679, 0.7826086957, 0.7779614325, 
          0.7797335871, 0.7875210793, 0.8059701493, 0.8514588859),
  sensitivity = c(0.03881787413, 0.02839463733, 0.0199065184, 0.01329622947, 0.008288701862, 0.004872239719, 
                  0.002790450992, 0.001516354971, 0.0007816868803, 0.0003365344167),
  F1 = c(0.04796917668, 0.04663504968, 0.0357071658, 0.02494878842, 0.01596855423, 0.009535245509, 
         0.00551108466, 0.003011220381, 0.001557100679, 0.0006715473771)
)

# Define your custom color palette
custom_palette <- c(
  "precision" = "#332288",       # Purple/Blue
  "FDR" = "#117733",             # Green
  "sensitivity" = "#DDCC77",     # Yellow
  "F1" = "#CC6677"              # Red
)

# Reshape the data into a long format for easier plotting with ggplot2
data_long <- reshape(data, 
                     varying = c("precision", "FDR", "sensitivity", "F1"),
                     v.names = "value", 
                     timevar = "metric", 
                     times = c("precision", "FDR", "sensitivity", "F1"),
                     direction = "long")

# Plot the data using ggplot2
p <- ggplot(data_long, aes(x = X_or_more_reads, y = value, color = metric, group = metric)) +
  geom_line(size = 1) +  # Plot lines
  geom_point(size = 3) + # Add points for each data value
  scale_color_manual(values = custom_palette) +  # Apply custom color palette
  labs( x = "X or More Reads", 
       y = "Value", 
       color = "Metric") +
  theme_minimal() +
    theme(
     legend.position = "bottom",  # Place legend to the right
      legend.text = element_text(size = 12),  # Smaller font size for the legend
     legend.title = element_text(size = 12),  # Slightly larger font size for the legend title
      legend.key.size = unit(0.5, "lines"),  # Smaller legend keys
      legend.box.spacing = unit(0.5, "cm"),  # Adjust spacing between the legend and plot
      text = element_text(size = 12),  # Set font size to 12pt for all text elements
      plot.margin = margin(10, 20, 10, 10)  # Increase margin to ensure the legend fits
  ) +
  guides(color = guide_legend(nrow = 3, byrow = TRUE))  # Arrange legend in 2 rows

# Save the plot with a width of 85mm (3.35 inches) and height of 75mm (2.95 inches)
ggsave("xormore_reads_plot_no_power_of_discovery.png", plot = p, width = 85 / 25.4, height = 75 / 25.4, units = "in", dpi = 300)   # Save as 85mm width

# Optionally, you can display the plot
print(p)




```


```{r}
# Load necessary library
library(ggplot2)

# Create the data frame
data <- data.frame(
  X_or_more_reads = 1:10,
  precision = c(0.06276631791, 0.1304073255, 0.1731192611, 0.2018195321, 0.2173913043, 0.2220385675, 
                0.2202664129, 0.2124789207, 0.1940298507, 0.1485411141),
  FDR = c(0.9372336821, 0.8695926745, 0.8268807389, 0.7981804679, 0.7826086957, 0.7779614325, 
          0.7797335871, 0.7875210793, 0.8059701493, 0.8514588859),
  sensitivity = c(0.03881787413, 0.02839463733, 0.0199065184, 0.01329622947, 0.008288701862, 0.004872239719, 
                  0.002790450992, 0.001516354971, 0.0007816868803, 0.0003365344167),
  F1 = c(0.04796917668, 0.04663504968, 0.0357071658, 0.02494878842, 0.01596855423, 0.009535245509, 
         0.00551108466, 0.003011220381, 0.001557100679, 0.0006715473771)
)

# Reshape the data into a long format for easier plotting with ggplot2
data_long <- reshape(data, 
                     varying = c("precision", "FDR", "sensitivity", "F1"),
                     v.names = "value", 
                     timevar = "metric", 
                     times = c("precision", "FDR", "sensitivity", "F1"),
                     direction = "long")

# Plot the data using ggplot2
ggplot(data_long, aes(x = X_or_more_reads, y = value, color = metric, group = metric)) +
  geom_line(size = 1) +  # Plot lines
  geom_point(size = 3) + # Add points for each data value
  labs(title = "Performance Metrics vs. X or More Reads", 
       x = "X or More Reads", 
       y = "Value", 
       color = "Metric") +
  theme_minimal() + 
  theme(text = element_text(size = 12))  # Set font size for all labels



```


```{r}
# Load necessary libraries
library(ggplot2)
library(reshape2)

# Create the data frame
data <- data.frame(
  distance_to_TE = c("40,40", "50,30", "30,50", "60,40", "40,60", "50,50", "30,30", "40,20", "20,40"),
  precision = c(0.271563214, 0.06118155857, 0.06118155857, 0.08537436327, 0.130556478, 0.1100544182, 0.05312938228, 0.04665110464, 0.06726828448),
  FDR = c(0.731056584, 0.9388184414, 0.9388184414, 0.9146256367, 0.869443522, 0.8899455818, 0.9468706177, 0.9533488954, 0.9327317155),
  sensitivity = c(0.2468157121, 0.4637035717, 0.4637035717, 0.4371204001, 0.2455389008, 0.379128727, 0.477305218, 0.4767265255, 0.4648856326),
  F1 = c(0.171547081, 0.1081002513, 0.1081002513, 0.1428488033, 0.1704710874, 0.170589653, 0.09561567582, 0.08498574546, 0.117530128),
  power_of_discovery = c(0.2468157121, 0.4637035717, 0.4637035717, 0.4386746237, 0.2468157121, 0.3805112675, 0.478934711, 0.478311214, 0.4665538434)
)

# Remove the power_of_discovery column
data <- data[, !names(data) %in% "power_of_discovery"]

# Reshape the data for ggplot
data_long <- melt(data, id.vars = "distance_to_TE", variable.name = "Metric", value.name = "Value")

# Define your custom color palette
custom_palette <- c("#332288", "#117733", "#DDCC77", "#CC6677", "#AA4499")

# Create the plot with the custom color palette
p <- ggplot(data_long, aes(x = distance_to_TE, y = Value, fill = Metric)) +
  geom_bar(stat = "identity", position = "dodge") +
  scale_fill_manual(values = custom_palette) +  # Apply the custom color palette
  theme_minimal() +
  labs(x = "Distance into TE, Genome",
       y = "Metric Value",
       fill = "Metric") +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),  # Rotate x-axis labels for better readability
    legend.position = "bottom",  # Place the legend to the right
    legend.text = element_text(size = 8),  # Smaller font size for the legend
    legend.title = element_text(size = 10),  # Slightly larger font size for the legend title
    legend.key.size = unit(0.5, "lines"),  # Smaller legend keys
    legend.box.spacing = unit(0.5, "cm"),  # Adjust spacing between the legend and plot
    text = element_text(size = 12),  # Set font size to 12pt for all text elements
    plot.margin = margin(10, 20, 10, 10)  # Increase margin to ensure the legend fits
  ) +
  guides(fill = guide_legend(nrow = 3, byrow = TRUE))  # Arrange legend in 3 rows

# Save the plot with a width of 85mm (3.35 inches) and height of 75mm (2.95 inches)
ggsave("dist_into_TEGenome_plot_no_power_of_discovery.png", plot = p, width = 85 / 25.4, height = 75 / 25.4, units = "in", dpi = 300)  # Save with specified dimensions

# Optionally, you can display the plot
print(p)

```

```{r}
# Load necessary libraries
library(ggplot2)
library(reshape2)

# Create the data frame
data <- data.frame(
  Metric = c("precision", "FDR", "sensitivity", "F1", "power_of_discovery"),
  single = c(0.271563214, 0.731056584, 0.4491850004, 0.1297418284, 0.4491850004),
  paired = c(0.26325, 0.73675, 0.7759903781, 0.06093914645, 0.7345684511)
)

# Remove the power_of_discovery metric from the data
data <- data[!data$Metric %in% "power_of_discovery", ]

# Calculate the percent change between paired and single
data$percent_change = ((data$paired - data$single) / data$single) * 100

# Reorder the Metric factor to control the plot order
data$Metric <- factor(data$Metric, levels = c("precision", "FDR", "sensitivity", "F1"))

# Reshape the data for ggplot
data_long <- melt(data, id.vars = "Metric", variable.name = "Condition", value.name = "Value")

# Define a color palette with 4 distinct colors (one for each metric)
custom_palette <- c("#332288", "#117733", "#DDCC77", "#CC6677")

# Create the plot
p <- ggplot(data, aes(x = Metric, y = percent_change, fill = Metric)) +
  geom_bar(stat = "identity", position = "dodge") +
  scale_fill_manual(values = custom_palette) +  # Apply the custom color palette
  theme_minimal() +
  labs(x = "Metric",
       y = "Percent Change between\nSE and PE (%)") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +  # Rotate x-axis labels for better readability
  theme(aspect.ratio = 1/3) +  # Adjust aspect ratio to make it skinnier
  theme(
    text = element_text(size = 12),  # Set font size to 12pt for all text elements
    plot.margin = margin(10, 20, 10, 10),  # Increase margin if needed
    axis.title.y = element_text(size = 12)  # Set the y-axis label font size to 10pt
  ) +
  theme(legend.position = "none")  # Remove the legend

# Save the plot with custom dimensions (adjust width and height)
ggsave("percent_change_plot_no_power_of_discovery.png", plot = p, width = 85 / 25.4, height = 75 / 25.4, units = "in", dpi = 300)  # Save with specified dimensions in inches

# Print the plot
print(p)


```
```{r}
# Load necessary libraries
library(ggplot2)
library(reshape2)

# Create the data frame
data <- data.frame(
  window = c(0, 5, 10, 20, 50, 75, 100, 125, 150, 200, 500),
  sensitivity = c(0.03881787413, 0.05991878067, 0.06807461056, 0.07109147834, 0.0752068353, 0.08338, 0.1278093747, 0.1404594435, 0.144533482, 0.1508971695, 0.1780388218),
  precision = c(0.06276696238, 0.09453548546, 0.1068362905, 0.1112103664, 0.1169500575, 0.128419172, 0.1910526532, 0.2081177099, 0.2129743716, 0.2207060128, 0.2511705274),
  F1 = c(0.04796936489, 0.07334793866, 0.08316049856, 0.0867364712, 0.09154439984, 0.1011107877, 0.1531591598, 0.1677223962, 0.1722028045, 0.1792444963, 0.2083743276),
  FDR = c(0.9372330376, 0.9054645145, 0.8931637095, 0.8887896336, 0.8830499425, 0.871580828, 0.8089473468, 0.7918822901, 0.7870256284, 0.7792939872, 0.7488294726),
  power_of_discovery = c(0.09074198664, 0.1322805036, 0.1443485992, 0.1498750541, 0.1586633188, 0.1740773223, 0.2372471046, 0.2549137392, 0.2625306358, 0.2734333702, 0.321597626)
)

# Remove the power_of_discovery metric from the data
data <- data[!names(data) %in% "power_of_discovery"]

# Reshape the data for ggplot
data_long <- melt(data, id.vars = "window", variable.name = "Metric", value.name = "Value")

# Reorder the Metric factor to control the plot order
data_long$Metric <- factor(data_long$Metric, levels = c("precision", "FDR", "sensitivity", "F1"))

# Define a custom color palette
custom_palette <- c("#332288", "#117733", "#DDCC77", "#CC6677")

# Create the line graph
p <- ggplot(data_long, aes(x = window, y = Value, color = Metric, group = Metric)) +
  geom_line() +
  geom_point() +
  scale_color_manual(values = custom_palette) +  # Apply the custom color palette
  theme_minimal() +
  labs(x = "Window Size",
       y = "Metric Value",
       color = "Metric") +
  theme(
    legend.position = "bottom",  # Place the legend at the bottom
    text = element_text(size = 12),  # Set font size to 12pt for all text elements
    axis.title.y = element_text(size = 10),  # Set y-axis label font size to 10pt
    plot.margin = margin(10, 20, 10, 10)  # Increase margin if needed
  ) +
  guides(color = guide_legend(nrow = 3, byrow = TRUE))  # Arrange legend in 3 rows

# Save the plot with custom dimensions (adjust width and height)
ggsave("line_plot_no_power_of_discovery.png", plot = p, width = 85 / 25.4, height = 75 / 25.4, units = "in", dpi = 300)  # Save with specified dimensions in inches

# Print the plot
print(p)


```


```{r}
# Load necessary libraries
library(ggplot2)
library(reshape2)

# Create the data frame
data <- data.frame(
  Condition = c("SWIFTE_15x", "SWIFTE_30x"),
  precision = c(0.254327335, 0.1792791749),
  FDR = c(0.745672665, 0.8207208251),
  sensitivity = c(0.1321813485, 0.2615384615),
  F1 = c(0.1739538155, 0.2127337734),
  power_of_discovery = c(0.1321813485, 0.2615384615)
)

# Remove the power_of_discovery metric from the data
data <- data[!names(data) %in% "power_of_discovery"]

# Reshape the data for ggplot
data_long <- melt(data, id.vars = "Condition", variable.name = "Metric", value.name = "Value")

# Define a custom color palette
custom_palette <- c("#332288", "#117733", "#DDCC77", "#CC6677")

# Create the bar graph
p <- ggplot(data_long, aes(x = Condition, y = Value, fill = Metric)) +
  geom_bar(stat = "identity", position = "dodge") +  # Create bars with dodging for each metric
  scale_fill_manual(values = custom_palette) +  # Apply the custom color palette
  theme_minimal() +
  labs(y = "Metric Value",
       fill = "Metric") +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),  # Rotate x-axis labels for better readability
    text = element_text(size = 12)  # Set font size to 12pt for all text elements
  )

# Save the plot with custom dimensions (adjust width and height)
ggsave("SWIFTE_readepth_plot_without_pod.png", plot = p, width = 85 / 25.4, height = 75 / 25.4, units = "in", dpi = 300)  # Save with specified dimensions in inches

# Print the plot
print(p)

```

```{r}
# Load necessary libraries
library(ggplot2)
library(reshape2)

# Create the data frame
data <- data.frame(
  Condition = c("SWIFTE_15x", "SWIFTE_30x"),
  precision = c(0.254327335, 0.1792791749),
  FDR = c(0.745672665, 0.8207208251),
  sensitivity = c(0.1321813485, 0.2615384615),
  F1 = c(0.1739538155, 0.2127337734),
  power_of_discovery = c(0.1321813485, 0.2615384615)
)

# Remove the power_of_discovery metric from the data
data <- data[!names(data) %in% "power_of_discovery"]

# Reshape the data for ggplot
data_long <- melt(data, id.vars = "Condition", variable.name = "Metric", value.name = "Value")

# Define a custom color palette
custom_palette <- c("#332288", "#117733", "#DDCC77", "#CC6677")

# Create the bar graph
p <- ggplot(data_long, aes(x = Condition, y = Value, fill = Metric)) +
  geom_bar(stat = "identity", position = "dodge") +  # Create bars with dodging for each metric
  scale_fill_manual(values = custom_palette) +  # Apply the custom color palette
  theme_minimal() +
  labs(y = "Metric Value", fill = "Metric") +  # Remove x-axis label
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),  # Rotate x-axis labels for better readability
    text = element_text(size = 12),  # Set font size to 12pt for all text elements
    axis.title.x = element_blank()  # Remove x-axis label
  )

# Save the plot with custom dimensions (adjust width and height)
ggsave("SWIFTE_readepth_plot_without_pod.png", plot = p, width = 85 / 25.4, height = 75 / 25.4, units = "in", dpi = 300)  # Save with specified dimensions in inches

# Print the plot
print(p)

```
