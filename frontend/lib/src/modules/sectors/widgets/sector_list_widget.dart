import 'package:flutter/material.dart';

class SectorsListWidget extends StatelessWidget {
  const SectorsListWidget({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;
    return ListView.separated(
      physics: const NeverScrollableScrollPhysics(),
      shrinkWrap: true,
      itemCount: 16,
      separatorBuilder: (_, __) => const Divider(),
      itemBuilder: (context, index) => const ListTile(
        visualDensity: VisualDensity.compact,
        title: Text('Nome do setor'),
        trailing: Text('15'),
      ),
    );
  }
}
