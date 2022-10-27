p.unscaled_log1p <- ggplot(data = p$data, mapping = aes(y = id, x = features.plot)) +
    geom_point(mapping=aes(size = pct.exp, color = MinMax(log1p(avg.exp),0,4))) +
    scale_size(range = c(0, 12), limits = c(0.1, 50)) +
    guides(
         size = guide_legend(title = "Percent Expressed"),
         color = guide_colourbar(title = "Average Expression")
    ) +
    cowplot::theme_cowplot() +
    RotatedAxis() +
    scale_color_gradientn(colours=COL1("YlGn")) +
    scale_y_discrete(limits=rev)